import logging
from typing import Union, Tuple

import vars
from models.bart import BartForClassificationAndGeneration
from data.vocab import Vocab

from downstream_tasks.summarization import run_summarization
from downstream_tasks.translation import run_translation

logger = logging.getLogger(__name__)


def train(
        args,
        task,
        trained_model: Union[BartForClassificationAndGeneration, str] = None,
        trained_vocab: Union[Tuple[Vocab, Vocab, Vocab], str] = None,
        only_test=False):
    """
    Fine-tuning from given pre-trained model and vocabs, or training from scratch.

    Args:
        args (argparse.Namespace): Arguments
        task (str): Training/Fine-tuning task, support ['summarization', 'translation', 'search']
        trained_model (Union[BartForClassificationAndGeneration, str]): Optional,
            instance or directory of ``BartForClassificationAndGeneration``, must given when ``only_test`` is True
        trained_vocab (Union[Tuple[Vocab, Vocab, Vocab], str]): Optional, Tuple of instances or directory of three
            vocabularies, must given when ``only_test`` is True
        only_test (bool): True when only need to test, default to False

    """
    assert task in [vars.SUMMARIZATION_TASK, vars.TRANSLATION_TASK, vars.SEARCH_TASK]
    assert not only_test or isinstance(trained_model, str) or \
           isinstance(trained_model, BartForClassificationAndGeneration), \
           f'The model type is not supported, expect Bart model or string of path, got {type(trained_model)}'
    assert not only_test or isinstance(trained_vocab, str) or isinstance(trained_vocab, tuple), \
        f'The vocab type is not supported, expect tuple or string of path, got {type(trained_vocab)}'
    assert (trained_model is None and trained_vocab is None) or \
           (trained_model is not None and trained_vocab is not None), \
           'Parameters ``trained_model`` and ``trained_vocab`` must given or not given simultaneously'

    logger.info('*' * 100)
    if trained_model:
        logger.info('Fine-tuning from pre-trained model and vocab')
    else:
        logger.info('Training from scratch')

    # start downstream task
    if task == vars.SUMMARIZATION_TASK:
        run_summarization(args=args,
                          trained_model=trained_model,
                          trained_vocab=trained_vocab,
                          only_test=only_test)
    elif task == vars.TRANSLATION_TASK:
        run_translation(args=args,
                        trained_model=trained_model,
                        trained_vocab=trained_vocab,
                        only_test=only_test)
    elif task == vars.SEARCH_TASK:
        run_search
