import torch
from transformers import TrainerCallback, TrainingArguments, TrainerState, TrainerControl

import logging
from typing import Dict

from models.bart import BartForClassificationAndGeneration
from .timer import Timer
from .early_stopping import EarlyStopping
import enums


logger = logging.getLogger(__name__)


class LogStateCallBack(TrainerCallback):

    epoch_timer = Timer()
    map_step_epoch = {-1: -1}

    def on_epoch_begin(self,
                       args: TrainingArguments,
                       state: TrainerState,
                       control: TrainerControl,
                       **kwargs):
        self.epoch_timer.reset()
        logger.debug('-' * 100)
        logger.debug(f'Start epoch {state.epoch}')

    def on_epoch_end(self,
                     args: TrainingArguments,
                     state: TrainerState,
                     control: TrainerControl,
                     optimizer: torch.optim.Optimizer,
                     **kwargs):
        epoch = state.epoch - 1
        self.map_step_epoch[state.global_step] = epoch
        logger.debug('Epoch {} / step {} finished, time: {:.2f}s'.format(epoch,
                                                                         state.global_step,
                                                                         self.epoch_timer.time()))
        logger.debug('learning rate: {}'.format(optimizer.param_groups[0]['lr']))

    def on_evaluate(self,
                    args: TrainingArguments,
                    state: TrainerState,
                    control: TrainerControl,
                    metrics: Dict[str, float],
                    **kwargs):
        epoch = metrics.pop('epoch') - 1
        logger.debug(f'Evaluation after epoch {epoch} finished')
        for metric, score in metrics.items():
            logger.debug(f'{metric}: {score}')
        try:
            best_steps = int(state.best_model_checkpoint.split('-')[-1])
        except Exception:
            best_steps = -1
        logger.info(f'Best model at epoch {self.map_step_epoch[best_steps]} / step {best_steps}, '
                    f'scores: {state.best_metric}')
