from transformers import BartConfig, TrainingArguments, EarlyStoppingCallback, \
    IntervalStrategy, SchedulerType, BartForSequenceClassification

import logging
from typing import Union, Tuple
import os
import numpy as np

from models.bart import BartForClassificationAndGeneration
from data.vocab import Vocab, load_vocab, init_vocab
from data.dataset import init_dataset
from data.data_utils import load_clone_mapping
from utils.general import count_params, human_format, layer_wise_parameters
from eval.metrics import ir_metrics
from utils.callbacks import LogStateCallBack
from utils.trainer import CodeCLSTrainer
import enums

logger = logging.getLogger(__name__)


def run_clone_detection(
        args,
        trained_model: Union[BartForClassificationAndGeneration, str] = None,
        trained_vocab: Union[Tuple[Vocab, Vocab, Vocab], str] = None,
        only_test=False):
    """
    Fine-tuning from given pre-trained model and vocabs, or training from scratch.

    Args:
        args (argparse.Namespace): Arguments
        trained_model (Union[BartForClassificationAndGeneration, str]): Optional,
            instance or directory of ``BartForClassificationAndGeneration``, must given when ``only_test`` is True
        trained_vocab (Union[Tuple[Vocab, Vocab, Vocab], str]): Optional, Tuple of instances or directory of three
            vocabularies, must given when ``only_test`` is True
        only_test (bool): True when only need to test, default to False

    """
    logger.info('-' * 100)
    logger.info(f'Code clone detection on CodeCloneBench dataset')
    # --------------------------------------------------
    # datasets
    # --------------------------------------------------
    logger.info('-' * 100)
    logger.info('Loading datasets')
    code_mapping = load_clone_mapping(args.dataset_root)
    datasets = dict()
    splits = ['test'] if only_test else ['train', 'valid', 'test']
    for split in splits:
        datasets[split] = init_dataset(args=args,
                                       mode=enums.TRAINING_MODE_FINE_TUNE,
                                       task=enums.TASK_CLONE_DETECTION,
                                       split='test',
                                       clone_mapping=code_mapping)
        logger.info(f'The size of {split} set: {len(datasets[split])}')
    logger.info('Datasets loaded successfully')

    # --------------------------------------------------
    # vocabs
    # --------------------------------------------------
    logger.info('-' * 100)
    if trained_vocab:
        if isinstance(trained_vocab, tuple):
            logger.info('Vocabularies are passed through parameter')
            assert len(trained_vocab) == 3
            code_vocab, ast_vocab, nl_vocab = trained_vocab
        else:
            logger.info('Loading vocabularies from files')
            code_vocab = load_vocab(vocab_root=trained_vocab, name=args.code_vocab_name)
            ast_vocab = load_vocab(vocab_root=trained_vocab, name=args.ast_vocab_name)
            nl_vocab = load_vocab(vocab_root=trained_vocab, name=args.nl_vocab_name)
    else:
        logger.info('Building vocabularies')
        code_vocab = init_vocab(vocab_save_dir=args.vocab_save_dir,
                                name=args.code_vocab_name,
                                method=args.code_tokenize_method,
                                vocab_size=args.code_vocab_size,
                                datasets=[datasets['train'].codes_1, datasets['train'].codes_2],
                                ignore_case=True,
                                save_root=args.vocab_root)
        nl_vocab = init_vocab(vocab_save_dir=args.vocab_save_dir,
                              name=args.nl_vocab_name,
                              method=args.nl_tokenize_method,
                              vocab_size=args.nl_vocab_size,
                              datasets=[datasets['train'].names_1, datasets['train'].names_2],
                              ignore_case=True,
                              save_root=args.vocab_root,
                              index_offset=len(code_vocab))
        ast_vocab = init_vocab(vocab_save_dir=args.vocab_save_dir,
                               name=args.ast_vocab_name,
                               method='word',
                               datasets=[datasets['train'].asts_1, datasets['train'].asts_2],
                               save_root=args.vocab_root,
                               index_offset=len(code_vocab) + len(nl_vocab))
    logger.info(f'The size of code vocabulary: {len(code_vocab)}')
    logger.info(f'The size of nl vocabulary: {len(nl_vocab)}')
    logger.info(f'The size of ast vocabulary: {len(ast_vocab)}')
    logger.info('Vocabularies built successfully')

    # --------------------------------------------------
    # model
    # --------------------------------------------------
    logger.info('-' * 100)
    if trained_model:
        if isinstance(trained_model, BartForClassificationAndGeneration):
            logger.info('Model is passed through parameter')
            model = trained_model
        else:
            logger.info('Loading the model from file')
            config = BartConfig.from_json_file(os.path.join(trained_model, 'config.json'))
            model = BartForClassificationAndGeneration.from_pretrained(os.path.join(trained_model, 'pytorch_model.bin'),
                                                                       config=config)
    else:
        logger.info('Building the model')
        config = BartConfig(vocab_size=len(code_vocab) + len(nl_vocab) + len(ast_vocab),
                            max_position_embeddings=1024,
                            encoder_layers=args.n_layer,
                            encoder_ffn_dim=args.d_ff,
                            encoder_attention_heads=args.n_head,
                            decoder_layers=args.n_layer,
                            decoder_ffn_dim=args.d_ff,
                            decoder_attention_heads=args.n_head,
                            activation_function='gelu',
                            d_model=args.d_model,
                            dropout=args.dropout,
                            use_cache=True,
                            pad_token_id=Vocab.START_VOCAB.index(Vocab.PAD_TOKEN),
                            bos_token_id=Vocab.START_VOCAB.index(Vocab.SOS_TOKEN),
                            eos_token_id=Vocab.START_VOCAB.index(Vocab.EOS_TOKEN),
                            is_encoder_decoder=True,
                            decoder_start_token_id=Vocab.START_VOCAB.index(Vocab.SOS_TOKEN),
                            forced_eos_token_id=Vocab.START_VOCAB.index(Vocab.EOS_TOKEN),
                            max_length=args.max_nl_len,
                            min_length=1,
                            num_beams=args.beam_width,
                            num_labels=2)
        model = BartForSequenceClassification(config)
        # model = BartForClassificationAndGeneration(config)
    # model.set_model_mode(enums.MODEL_MODE_CLS)
    # log model statistics
    logger.info('Trainable parameters: {}'.format(human_format(count_params(model))))
    table = layer_wise_parameters(model)
    logger.debug('Layer-wised trainable parameters:\n{}'.format(table))
    logger.info('Model built successfully')

    # --------------------------------------------------
    # trainer
    # --------------------------------------------------
    logger.info('-' * 100)
    logger.info('Initializing the running configurations')

    # compute metrics
    def compute_valid_metrics(eval_preds):
        preds, labels = eval_preds
        if isinstance(preds, tuple):
            preds = preds[0]
        preds = np.argmax(preds, axis=1).tolist()
        result = {}
        result.update(ir_metrics(references=labels, candidates=preds))
        return result

    def compute_test_metrics(eval_preds):
        preds, labels = eval_preds
        if isinstance(preds, tuple):
            preds = preds[0]
        preds = np.argmax(preds, axis=1).tolist()
        result = {}
        result.update(ir_metrics(references=labels, candidates=preds))
        result.update({'refs': labels, 'cans': preds})
        return result

    training_args = TrainingArguments(output_dir=os.path.join(args.checkpoint_root, enums.TASK_CLONE_DETECTION),
                                      overwrite_output_dir=True,
                                      do_train=True,
                                      do_eval=True,
                                      do_predict=True,
                                      evaluation_strategy=IntervalStrategy.EPOCH,
                                      prediction_loss_only=False,
                                      per_device_train_batch_size=args.batch_size,
                                      per_device_eval_batch_size=args.eval_batch_size,
                                      gradient_accumulation_steps=args.gradient_accumulation_steps,
                                      learning_rate=args.learning_rate,
                                      weight_decay=args.lr_decay_rate,
                                      max_grad_norm=args.grad_clipping_norm,
                                      num_train_epochs=args.n_epoch,
                                      lr_scheduler_type=SchedulerType.LINEAR,
                                      warmup_steps=args.warmup_steps,
                                      logging_dir=os.path.join(args.tensor_board_root,
                                                               enums.TASK_CLONE_DETECTION),
                                      logging_strategy=IntervalStrategy.STEPS,
                                      logging_steps=args.logging_steps,
                                      save_strategy=IntervalStrategy.EPOCH,
                                      save_total_limit=5,
                                      seed=args.random_seed,
                                      fp16=args.fp16,
                                      dataloader_drop_last=False,
                                      run_name=args.model_name,
                                      load_best_model_at_end=True,
                                      metric_for_best_model='f1',
                                      greater_is_better=True,
                                      ignore_data_skip=False,
                                      label_smoothing_factor=args.label_smoothing,
                                      report_to=['tensorboard'],
                                      dataloader_pin_memory=True)
    trainer = CodeCLSTrainer(main_args=args,
                             code_vocab=code_vocab,
                             ast_vocab=ast_vocab,
                             nl_vocab=nl_vocab,
                             task=enums.TASK_CLONE_DETECTION,
                             model=model,
                             args=training_args,
                             data_collator=None,
                             train_dataset=datasets['train'] if 'train' in datasets else None,
                             eval_dataset=datasets['valid'] if 'valid' in datasets else None,
                             tokenizer=nl_vocab,
                             model_init=None,
                             compute_metrics=compute_valid_metrics,
                             callbacks=[
                                 EarlyStoppingCallback(early_stopping_patience=args.early_stop_patience),
                                 LogStateCallBack()])
    logger.info('Running configurations initialized successfully')

    # --------------------------------------------------
    # train
    # --------------------------------------------------
    if not only_test:
        logger.info('-' * 100)
        logger.info('Start training')
        train_result = trainer.train()
        logger.info('Training finished')
        trainer.save_model(args.model_root)
        trainer.save_state()
        metrics = train_result.metrics
        trainer.log_metrics(split='train', metrics=metrics)
        trainer.save_metrics(split='train', metrics=metrics)

    # --------------------------------------------------
    # predict
    # --------------------------------------------------
    logger.info('-' * 100)
    logger.info('Start testing')
    trainer.compute_metrics = compute_test_metrics
    predict_results = trainer.predict(test_dataset=datasets['test'],
                                      metric_key_prefix='test')
    predict_metrics = predict_results.metrics
    references = predict_metrics.pop('test_refs')
    candidates = predict_metrics.pop('test_cans')
    trainer.log_metrics(split='test', metrics=predict_metrics)
    trainer.save_metrics(split='test', metrics=predict_metrics)
    # save testing results
    with open(os.path.join(args.output_root, f'{enums.TASK_CLONE_DETECTION}_test_results.txt'),
              mode='w', encoding='utf-8') as f:
        f.write('#\ttrue\tpred\n')
        sample_id = 0
        for reference, candidate in zip(references, candidates):
            f.write(f'{sample_id}\t{reference}\t{candidate}\n')
            sample_id += 1
        for name, score in predict_metrics.items():
            f.write(f'{name}: {score}\n')
    logger.info('Testing finished')
    for name, score in predict_metrics.items():
        logger.info(f'{name}: {score}')
