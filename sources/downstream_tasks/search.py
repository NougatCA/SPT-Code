from transformers import BartConfig, TrainingArguments, IntervalStrategy, SchedulerType
from torch.utils.data.dataloader import DataLoader

import logging
from typing import Union, Tuple
import os

import enums
from models.bart import BartForClassificationAndGeneration
from data.vocab import Vocab, load_vocab, init_vocab
from data.dataset import init_dataset
from utils.general import count_params, human_format, layer_wise_parameters
from utils.callbacks import LogStateCallBack, SearchValidCallBack
from utils.trainer import CodeCLSTrainer
from data.data_collator import collate_fn

logger = logging.getLogger(__name__)


def run_search(
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
    logger.info(f'Code search on language: {args.search_language}')
    # --------------------------------------------------
    # datasets
    # --------------------------------------------------
    logger.info('-' * 100)
    logger.info('Loading datasets')
    datasets = dict()
    splits = ['codebase', 'test'] if only_test else ['codebase', 'train', 'valid', 'test']
    for split in splits:
        datasets[split] = init_dataset(args=args,
                                       mode=enums.TRAINING_MODE_FINE_TUNE,
                                       task=enums.TASK_SEARCH,
                                       language=args.search_language,
                                       split=split)
        logger.info(f'The size of {split} set: {len(datasets[split])}')
    codebase_dataloader = DataLoader(dataset=datasets['codebase'],
                                     batch_size=args.eval_batch_size,
                                     collate_fn=lambda batch: collate_fn(batch,
                                                                         args=args,
                                                                         task=enums.TASK_SEARCH,
                                                                         code_vocab=code_vocab,
                                                                         nl_vocab=nl_vocab,
                                                                         ast_vocab=ast_vocab))
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
                                datasets=[datasets['train'].codes],
                                ignore_case=True,
                                save_root=args.vocab_root)
        nl_vocab = init_vocab(vocab_save_dir=args.vocab_save_dir,
                              name=args.nl_vocab_name,
                              method=args.nl_tokenize_method,
                              vocab_size=args.nl_vocab_size,
                              datasets=[datasets['train'].nls],
                              ignore_case=True,
                              save_root=args.vocab_root,
                              index_offset=len(code_vocab))
        ast_vocab = init_vocab(vocab_save_dir=args.vocab_save_dir,
                               name=args.ast_vocab_name,
                               method='word',
                               datasets=[datasets['train'].asts],
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
        config = BartConfig(vocab_size=len(code_vocab) + len(ast_vocab) + len(nl_vocab),
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
                            max_length=args.max_code_len,
                            min_length=1,
                            num_beams=args.beam_width,
                            num_labels=2)
        model = BartForClassificationAndGeneration(config, mode=enums.MODEL_MODE_SEARCH)
    model.set_model_mode(enums.MODEL_MODE_SEARCH)
    # log model statistic
    logger.info('Trainable parameters: {}'.format(human_format(count_params(model))))
    table = layer_wise_parameters(model)
    logger.debug('Layer-wised trainable parameters:\n{}'.format(table))
    logger.info('Model built successfully')

    # --------------------------------------------------
    # trainer
    # --------------------------------------------------
    if not only_test:
        logger.info('-' * 100)
        logger.info('Initializing the running configurations')

        valid_dataloader = DataLoader(dataset=datasets['valid'],
                                      batch_size=args.eval_batch_size,
                                      collate_fn=lambda batch: collate_fn(batch,
                                                                          args=args,
                                                                          task=enums.TASK_SEARCH,
                                                                          code_vocab=code_vocab,
                                                                          nl_vocab=nl_vocab,
                                                                          ast_vocab=ast_vocab))
        training_args = TrainingArguments(output_dir=os.path.join(args.checkpoint_root, enums.TASK_SEARCH),
                                          overwrite_output_dir=True,
                                          do_train=True,
                                          do_eval=False,
                                          do_predict=False,
                                          evaluation_strategy=IntervalStrategy.NO,
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
                                          logging_dir=os.path.join(args.tensor_board_root, enums.TASK_SEARCH),
                                          logging_strategy=IntervalStrategy.STEPS,
                                          logging_steps=args.logging_steps,
                                          save_strategy=IntervalStrategy.EPOCH,
                                          save_total_limit=5,
                                          seed=args.random_seed,
                                          fp16=args.fp16,
                                          dataloader_drop_last=False,
                                          run_name=args.model_name,
                                          load_best_model_at_end=True,
                                          metric_for_best_model=None,
                                          greater_is_better=None,
                                          ignore_data_skip=False,
                                          label_smoothing_factor=args.label_smoothing,
                                          report_to=['tensorboard'],
                                          dataloader_pin_memory=True)
        trainer = CodeCLSTrainer(main_args=args,
                                 code_vocab=code_vocab,
                                 ast_vocab=ast_vocab,
                                 nl_vocab=nl_vocab,
                                 task=enums.TASK_SEARCH,
                                 model=model,
                                 args=training_args,
                                 data_collator=None,
                                 train_dataset=datasets['train'],
                                 eval_dataset=None,
                                 tokenizer=nl_vocab,
                                 model_init=None,
                                 compute_metrics=None,
                                 callbacks=[
                                     LogStateCallBack(),
                                     SearchValidCallBack(codebase_dataloader=codebase_dataloader,
                                                         eval_dataloader=valid_dataloader,
                                                         early_stop_patience=args.early_stop_patience)])
        logger.info('Running configurations initialized successfully')

        # --------------------------------------------------
        # train
        # --------------------------------------------------
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
    test_dataloader = DataLoader(dataset=datasets['test'],
                                 batch_size=args.eval_batch_size,
                                 collate_fn=lambda batch: collate_fn(batch,
                                                                     args=args,
                                                                     task=enums.TASK_SEARCH,
                                                                     code_vocab=code_vocab,
                                                                     nl_vocab=nl_vocab,
                                                                     ast_vocab=ast_vocab))
    predict_metrics = model.evaluate_search(query_dataloader=test_dataloader,
                                            codebase_dataloader=codebase_dataloader,
                                            metrics_prefix='test')
    ranks = predict_metrics.pop('test_ranks')
    ref_urls = predict_metrics.pop('test_ref_urls')
    can_urls = predict_metrics.pop('test_can_urls')
    can_sims = predict_metrics.pop('test_can_sims')
    trainer.log_metrics(split='test', metrics=predict_metrics)
    trainer.save_metrics(split='test', metrics=predict_metrics)
    # save testing results
    with open(os.path.join(args.output_root, f'{enums.TASK_SEARCH}_test_results.txt'),
              mode='w', encoding='utf-8') as result_f, \
            open(os.path.join(args.output_root, f'{enums.TASK_SEARCH}_test_refs.txt'),
                 mode='w', encoding='utf-8') as refs_f, \
            open(os.path.join(args.output_root, f'{enums.TASK_SEARCH}_test_cans.txt'),
                 mode='w', encoding='utf-8') as cans_f:
        sample_id = 0
        for rank, ref_url, can_url, can_sim in zip(ranks, ref_urls, can_urls, can_sims):
            result_f.write(f'sample {sample_id}:\n')
            sample_id += 1
            result_f.write(f'rank: {rank}\n')
            result_f.write(f'reference_url: {ref_url}\n')
            result_f.write(f'first_candidate_url: {can_url}\n')
            result_f.write(f'first_candidate_similarity: {can_sim}\n')
            result_f.write('\n')
            refs_f.write(ref_url + '\n')
            cans_f.write(can_url + '\n')
        for name, score in predict_metrics.items():
            result_f.write(f'{name}: {score}\n')
    logger.info('Testing finished')
    for name, score in predict_metrics.items():
        logger.info(f'{name}: {score}')
