import torch

import argparse
import random
import numpy as np
import logging
import os
import sys
import time
from prettytable import PrettyTable

from args import add_args
from train import train
from pre_train import pre_train
import enums
from data.dataset import save_all_datasets


def remake(main_args):
    main_args.output_root = os.path.join(
        '..',
        'outputs',
        '{}_{}'.format(main_args.model_name, time.strftime('%Y%m%d_%H%M%S', time.localtime())))
    # Root for outputs during pre-training
    main_args.pre_train_output_root = os.path.join(main_args.output_root, 'pre_train')
    # Root for saving checkpoints
    main_args.checkpoint_root = os.path.join(main_args.output_root, 'checkpoints')
    # Root for saving models
    main_args.model_root = os.path.join(main_args.output_root, 'models')
    # Root for saving vocabs
    main_args.vocab_root = os.path.join(main_args.output_root, 'vocabs')
    # Rot for tensorboard
    main_args.tensor_board_root = os.path.join(main_args.output_root, 'runs')
    for d in [main_args.checkpoint_root, main_args.model_root, main_args.vocab_root, main_args.tensor_board_root,
              main_args.dataset_save_dir, main_args.vocab_save_dir]:
        if not os.path.exists(d):
            os.makedirs(d)

    # log command and configs
    logger.debug('COMMAND: {}'.format(' '.join(sys.argv)))

    config_table = PrettyTable()
    config_table.field_names = ["Configuration", "Value"]
    config_table.align["Configuration"] = "l"
    config_table.align["Value"] = "l"
    for config, value in vars(main_args).items():
        config_table.add_row([config, str(value)])
    logger.debug('Configurations:\n{}'.format(config_table))

    return main_args


def main(args):

    # model, vocabs = pre_train(args, tasks=[enums.TASK_CODE_AST_PREDICTION, enums.TASK_METHOD_NAME_PREDICTION])
    # model, vocabs = pre_train(args)
    # train(args, trained_model=model, trained_vocab=vocabs)

    args.fp16 = True
    args.task = enums.TASK_TRANSLATION

    # no pre-training
    args.model_name = f'{args.task}_no_pre_train'
    args = remake(args)
    train(args, task=args.task)

    # no single pre-training task
    for pre_train_task in ['no_cap', 'no_mass', 'no_mng']:
        args.model_name = f'{args.task}_{pre_train_task}'
        args = remake(args)
        train(args,
              task=args.task,
              trained_model=f'../pre_trained/models/{pre_train_task}/',
              trained_vocab='../pre_trained/vocabs/')

    # no ast
    args.no_ast = True
    args.no_nl = False
    args.model_name = f'{args.task}_no_ast'
    args = remake(args)
    train(args,
          task=args.task,
          trained_model=f'../pre_trained/models/all/',
          trained_vocab='../pre_trained/vocabs/')

    # no nl
    args.no_ast = False
    args.no_nl = True
    args.model_name = f'{args.task}_no_nl'
    args = remake(args)
    train(args,
          task=args.task,
          trained_model=f'../pre_trained/models/all/',
          trained_vocab='../pre_trained/vocabs/')

    # only code
    args.no_ast = True
    args.no_nl = True
    args.model_name = f'{args.task}_only_code'
    args = remake(args)
    train(args,
          task=args.task,
          trained_model=f'../pre_trained/models/all/',
          trained_vocab='../pre_trained/vocabs/')

    # only init dataset and save
    # save_all_datasets(args)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.register('type', 'bool', lambda v: v.lower() in ['yes', 'true', 't', '1', 'y'])

    add_args(parser)

    main_args = parser.parse_args()

    # define and make dirs
    # Root directory for the output of this run
    main_args.output_root = os.path.join(
        '..',
        'outputs',
        '{}_{}'.format(main_args.model_name, time.strftime('%Y%m%d_%H%M%S', time.localtime())))
    # Root for outputs during pre-training
    main_args.pre_train_output_root = os.path.join(main_args.output_root, 'pre_train')
    # Root for saving checkpoints
    main_args.checkpoint_root = os.path.join(main_args.output_root, 'checkpoints')
    # Root for saving models
    main_args.model_root = os.path.join(main_args.output_root, 'models')
    # Root for saving vocabs
    main_args.vocab_root = os.path.join(main_args.output_root, 'vocabs')
    # Rot for tensorboard
    main_args.tensor_board_root = os.path.join(main_args.output_root, 'runs')
    for d in [main_args.checkpoint_root, main_args.model_root, main_args.vocab_root, main_args.tensor_board_root,
              main_args.dataset_save_dir, main_args.vocab_save_dir]:
        if not os.path.exists(d):
            os.makedirs(d)

    # cuda and parallel
    if main_args.cuda_visible_devices is not None:
        os.environ['CUDA_VISIBLE_DEVICES'] = main_args.cuda_visible_devices
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    main_args.use_cuda = torch.cuda.is_available()
    main_args.parallel = torch.cuda.device_count() > 1

    # set random seed
    if main_args.random_seed > 0:
        random.seed(main_args.random_seed)
        np.random.seed(main_args.random_seed)
        torch.manual_seed(main_args.random_seed)
        torch.cuda.manual_seed_all(main_args.random_seed)

    # logging, log to both console and file, debug level only to file
    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(level=logging.INFO)
    logger.addHandler(console)

    file = logging.FileHandler(os.path.join(main_args.output_root, 'info.log'))
    file.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s | %(filename)s | line %(lineno)d] - %(levelname)s: %(message)s')
    file.setFormatter(formatter)
    logger.addHandler(file)

    # log command and configs
    logger.debug('COMMAND: {}'.format(' '.join(sys.argv)))

    config_table = PrettyTable()
    config_table.field_names = ["Configuration", "Value"]
    config_table.align["Configuration"] = "l"
    config_table.align["Value"] = "l"
    for config, value in vars(main_args).items():
        config_table.add_row([config, str(value)])
    logger.debug('Configurations:\n{}'.format(config_table))

    # run
    main(main_args)
