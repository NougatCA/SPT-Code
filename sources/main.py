import torch

import argparse
import random
import numpy as np
import logging
import os
import sys
from prettytable import PrettyTable

from args import add_args
from train import train
from pre_train import pre_train


def main(args):
    model, vocabs = pre_train(args)
    # train(args, trained_model=model, trained_vocab=vocabs)

    # train(args)
    # train(args,
    #       model_dir='../outputs/default_model_20210622_095911/models/',
    #       vocab_dir='../outputs/default_model_20210622_095911/vocabs/',
    #       only_test=True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.register('type', 'bool', lambda v: v.lower() in ['yes', 'true', 't', '1', 'y'])

    add_args(parser)

    main_args = parser.parse_args()

    # make dirs
    for d in [main_args.checkpoint_root, main_args.model_root, main_args.vocab_root, main_args.tensor_board_root]:
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
