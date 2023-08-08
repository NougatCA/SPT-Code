import torch
import torch.nn as nn
from torch.optim import AdamW
from transformers import BartConfig, get_scheduler, SchedulerType
from torch.utils.data.dataloader import DataLoader
from accelerate import Accelerator

import logging
from typing import Union, Tuple
import os
import math
from tqdm import tqdm
import numpy as np

import enums
from models.bart import BartForClassificationAndGeneration
from data.vocab import Vocab, load_vocab, init_vocab
from data.dataset import init_dataset
from utils.general import count_params, human_format, layer_wise_parameters
from data.data_collator import collate_fn
from utils.early_stopping import EarlyStopping

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
    # accelerator
    accelerator = Accelerator()
    logger.info(accelerator.state)
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
        model = BartForClassificationAndGeneration(config, mode=enums.MODEL_MODE_GEN)
    model.set_model_mode(enums.MODEL_MODE_GEN)
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
        gradient_accumulation_steps = 1
        # dataloader
        dataloader = DataLoader(dataset=datasets['train'],
                                batch_size=args.batch_size,
                                collate_fn=lambda batch: collate_fn(batch,
                                                                    args=args,
                                                                    task=enums.TASK_SEARCH,
                                                                    code_vocab=code_vocab,
                                                                    nl_vocab=nl_vocab,
                                                                    ast_vocab=ast_vocab))
        valid_dataloader = DataLoader(dataset=datasets['valid'],
                                      batch_size=args.eval_batch_size,
                                      collate_fn=lambda batch: collate_fn(batch,
                                                                          args=args,
                                                                          task=enums.TASK_SEARCH,
                                                                          code_vocab=code_vocab,
                                                                          nl_vocab=nl_vocab,
                                                                          ast_vocab=ast_vocab))
        # optimizer
        no_decay = ["bias", "LayerNorm.weight"]
        optimizer_grouped_parameters = [
            {
                "params": [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
                "weight_decay": args.lr_decay_rate,
            },
            {
                "params": [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)],
                "weight_decay": 0.0,
            },
        ]
        optimizer = AdamW(optimizer_grouped_parameters, lr=args.learning_rate)
        # Prepare everything with `accelerator`
        model, optimizer, dataloader, valid_dataloader, codebase_dataloader = accelerator.prepare(
            model, optimizer, dataloader, valid_dataloader, codebase_dataloader
        )
        # Scheduler and math around the number of training steps.
        num_update_steps_per_epoch = math.ceil(len(dataloader) / gradient_accumulation_steps)
        max_train_steps = args.n_epoch * num_update_steps_per_epoch

        lr_scheduler = get_scheduler(name=SchedulerType.LINEAR,
                                     optimizer=optimizer,
                                     num_warmup_steps=args.warmup_steps,
                                     num_training_steps=max_train_steps)
        # early stopping
        early_stopping = EarlyStopping(patience=args.early_stop_patience, higher_better=True)
        logger.info('Running configurations initialized successfully')

        # loss
        loss_fct = torch.nn.CrossEntropyLoss()

        # --------------------------------------------------
        # train
        # --------------------------------------------------
        logger.info('-' * 100)
        logger.info('Start training')

        total_batch_size = args.batch_size * accelerator.num_processes * gradient_accumulation_steps

        logger.info("***** Running training *****")
        logger.info(f"  Num examples = {len(datasets['train'])}")
        logger.info(f"  Num Epochs = {args.n_epoch}")
        logger.info(f"  Instantaneous batch size per device = {args.batch_size}")
        logger.info(f"  Total train batch size (w. parallel, distributed & accumulation) = {total_batch_size}")
        logger.info(f"  Gradient Accumulation steps = {gradient_accumulation_steps}")
        logger.info(f"  Total optimization steps = {max_train_steps}")

        progress_bar = tqdm(range(max_train_steps))
        completed_steps = 0

        for epoch in range(args.n_epoch):
            model.train()
            for step, batch in enumerate(dataloader):
                code_hidden_states = model(
                    input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    labels=batch["input_ids"],
                    decoder_attention_mask=batch["attention_mask"],
                    return_dict=True,
                    output_hidden_states=True
                ).decoder_hidden_states[-1]

                code_eos_mask = batch["input_ids"].eq(code_vocab.get_eos_index())
                if len(torch.unique_consecutive(code_eos_mask.sum(1))) > 1:
                    raise ValueError("All examples must have the same number of <eos> tokens.")
                code_vec = code_hidden_states[code_eos_mask, :].view(
                    code_hidden_states.size(0), -1, code_hidden_states.size(-1))[:, -1, :]
                code_vec = torch.nn.functional.normalize(code_vec, p=2, dim=1)

                nl_hidden_states = model(
                    input_ids=batch["nl_input_ids"],
                    attention_mask=batch["nl_attention_mask"],
                    labels=batch["nl_input_ids"],
                    decoder_attention_mask=batch["nl_attention_mask"],
                    return_dict=True,
                    output_hidden_states=True
                ).decoder_hidden_states[-1]
                nl_eos_mask = batch["nl_input_ids"].eq(nl_vocab.get_eos_index())
                if len(torch.unique_consecutive(nl_eos_mask.sum(1))) > 1:
                    raise ValueError("All examples must have the same number of <eos> tokens.")
                nl_vec = nl_hidden_states[nl_eos_mask, :].view(
                    nl_hidden_states.size(0), -1, nl_hidden_states.size(-1))[:, -1, :]
                nl_vec = torch.nn.functional.normalize(nl_vec, p=2, dim=1)

                # calculate scores and loss
                scores = torch.einsum("ab,cb->ac", nl_vec, code_vec)
                loss = loss_fct(scores * 20, torch.arange(batch["input_ids"].size(0), device=scores.device))

                loss = loss / gradient_accumulation_steps
                accelerator.backward(loss)

                if step % args.logging_steps == 0 and step != 0:
                    logger.info({
                        "global_step": completed_steps,
                        "epoch": completed_steps / num_update_steps_per_epoch,
                        "loss": loss.item(),
                    })

                if step % gradient_accumulation_steps == 0 or step == len(dataloader) - 1:
                    # Gradient clipping
                    if args.grad_clipping_norm is not None and args.grad_clipping_norm > 0:

                        if hasattr(optimizer, "clip_grad_norm"):
                            # Some optimizers (like the sharded optimizer) have a specific way to do gradient clipping
                            optimizer.clip_grad_norm(args.grad_clipping_norm)
                        elif hasattr(model, "clip_grad_norm_"):
                            # Some models (like FullyShardedDDP) have a specific way to do gradient clipping
                            model.clip_grad_norm_(args.grad_clipping_norm)
                        else:
                            # Revert to normal clipping otherwise, handling Apex or full precision
                            nn.utils.clip_grad_norm_(model.parameters(), args.grad_clipping_norm)

                    optimizer.step()
                    lr_scheduler.step()
                    optimizer.zero_grad()
                    progress_bar.update(1)
                    completed_steps += 1

                if completed_steps >= max_train_steps:
                    break

            model.eval()
            logger.info("***** Running evaluation *****")
            logger.info("  Num queries = %d", len(datasets['valid']))
            logger.info("  Num codes = %d", len(datasets['codebase']))
            logger.info("  Batch size = %d", args.eval_batch_size)
            valid_result = run_eval(
                args=args,
                model=model,
                query_dataloader=valid_dataloader,
                codebase_dataloader=codebase_dataloader,
                code_vocab=code_vocab,
                nl_vocab=nl_vocab,
                split="valid",
                epoch=epoch
            )
            logger.info(valid_result)
            mrr = valid_result['valid_mrr']
            early_stopping(score=mrr, model=model.state_dict(), epoch=epoch)
            if early_stopping.early_stop:
                break

        logger.info('Training finished')

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
    test_dataloader = accelerator.prepare(test_dataloader)
    if not only_test:
        model.load_state_dict(early_stopping.best_model)
    model.eval()
    logger.info("***** Running prediction *****")
    logger.info("  Num queries = %d", len(datasets['test']))
    logger.info("  Num codes = %d", len(datasets['codebase']))
    logger.info("  Batch size = %d", args.eval_batch_size)
    test_result = run_eval(
        args=args,
        model=model,
        query_dataloader=test_dataloader,
        codebase_dataloader=codebase_dataloader,
        code_vocab=code_vocab,
        nl_vocab=nl_vocab,
        split="test"
    )
    logger.info(test_result)
    logger.info('Testing finished')


def run_eval(
        args,
        model,
        query_dataloader,
        codebase_dataloader,
        code_vocab,
        nl_vocab,
        split,
        epoch=None
):
    assert split in ["valid", "test"]
    assert split == "test" or epoch is not None

    code_vecs = []
    nl_vecs = []

    code_urls = []
    nl_urls = []

    model.eval()
    for batch in tqdm(query_dataloader, desc="[1/3] Queries", ascii=True):
        with torch.no_grad():
            nl_hidden_states = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                labels=batch["input_ids"],
                decoder_attention_mask=batch["attention_mask"],
                return_dict=True,
                output_hidden_states=True
            ).decoder_hidden_states[-1]
            nl_eos_mask = batch["input_ids"].eq(nl_vocab.get_eos_index())
            if len(torch.unique_consecutive(nl_eos_mask.sum(1))) > 1:
                raise ValueError("All examples must have the same number of <eos> tokens.")
            nl_vec = nl_hidden_states[nl_eos_mask, :].view(
                nl_hidden_states.size(0), -1, nl_hidden_states.size(-1))[:, -1, :]
            nl_vec = torch.nn.functional.normalize(nl_vec, p=2, dim=1)
        nl_vecs.extend(nl_vec.cpu().numpy())
        nl_urls.extend(batch["urls"])

    for batch in tqdm(codebase_dataloader, desc="[2/3] Codes", ascii=True):
        with torch.no_grad():
            code_hidden_states = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                labels=batch["input_ids"],
                decoder_attention_mask=batch["attention_mask"],
                return_dict=True,
                output_hidden_states=True
            ).decoder_hidden_states[-1]

            code_eos_mask = batch["input_ids"].eq(code_vocab.get_eos_index())
            if len(torch.unique_consecutive(code_eos_mask.sum(1))) > 1:
                raise ValueError("All examples must have the same number of <eos> tokens.")
            code_vec = code_hidden_states[code_eos_mask, :].view(
                code_hidden_states.size(0), -1, code_hidden_states.size(-1))[:, -1, :]
            code_vec = torch.nn.functional.normalize(code_vec, p=2, dim=1)
        code_vecs.extend(code_vec.cpu().numpy())
        code_urls.extend(batch["urls"])

    code_vecs = np.array(code_vecs)
    nl_vecs = np.array(nl_vecs)

    scores = np.matmul(nl_vecs, code_vecs.T)
    sort_ids = np.argsort(scores, axis=-1, kind='quicksort', order=None)[:, ::-1]

    ranks = []
    for url, sort_id in tqdm(zip(nl_urls, sort_ids), desc="[3/3] Computing MRR", ascii=True):
        rank = 0
        find = False
        for idx in sort_id[:1000]:
            if find is False:
                rank += 1
            if code_urls[idx] == url:
                find = True
        if find:
            ranks.append(1 / rank)
        else:
            ranks.append(0)

    result = {
        f"{split}_mrr": float(np.mean(ranks)),
        f"{split}_num_queries": len(nl_vecs),
        f"{split}_num_codes": len(code_vecs),
    }

    model.train()

    return result



