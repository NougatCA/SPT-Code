import logging
from typing import Union, Tuple

import enums
from models.bart import BartForClassificationAndGeneration
from data.vocab import Vocab

from downstream_tasks.summarization import run_summarization
from downstream_tasks.translation import run_translation
from downstream_tasks.search import run_search
from downstream_tasks.clone import run_clone_detection
from downstream_tasks.completion import run_completion
from downstream_tasks.search_no_trainer import run_search_no_trainer

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
    assert task in [enums.TASK_SUMMARIZATION, enums.TASK_TRANSLATION, enums.TASK_SEARCH, enums.TASK_CLONE_DETECTION,
                    enums.TASK_COMPLETION]
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
        if isinstance(trained_model, str):
            logger.info(f'Model dir: {trained_model}')
        if isinstance(trained_vocab, str):
            logger.info(f'Vocab dir: {trained_vocab}')
    else:
        logger.info('Training from scratch')

    # start downstream task
    if task == enums.TASK_SUMMARIZATION:
        run_summarization(args=args,
                          trained_model=trained_model,
                          trained_vocab=trained_vocab,
                          only_test=only_test)
    elif task == enums.TASK_TRANSLATION:
        run_translation(args=args,
                        trained_model=trained_model,
                        trained_vocab=trained_vocab,
                        only_test=only_test)
    elif task == enums.TASK_SEARCH:
        # run_search(args=args,
        #            trained_model=trained_model,
        #            trained_vocab=trained_vocab,
        #            only_test=only_test)
        run_search_no_trainer(args=args,
                              trained_model=trained_model,
                              trained_vocab=trained_vocab,
                              only_test=only_test)
    elif task == enums.TASK_CLONE_DETECTION:
        run_clone_detection(args=args,
                            trained_model=trained_model,
                            trained_vocab=trained_vocab,
                            only_test=only_test)
    elif task == enums.TASK_COMPLETION:
        run_completion(args=args,
                       trained_model=trained_model,
                       trained_vocab=trained_vocab,
                       only_test=only_test)
