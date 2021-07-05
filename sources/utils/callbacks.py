import torch.optim
from transformers import TrainerCallback, TrainingArguments, TrainerState, TrainerControl

import logging

from .timer import Timer


logger = logging.getLogger(__name__)


class LogStateCallBack(TrainerCallback):

    epoch_timer = Timer()

    def on_epoch_begin(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, **kwargs):
        self.epoch_timer.reset()

    def on_epoch_end(self, args: TrainingArguments, state: TrainerState, control: TrainerControl,
                     optimizer: torch.optim.Optimizer, **kwargs):
        logger.debug('Epoch {} finished, time: {:.2f}s'.format(state.epoch, self.epoch_timer.time()))
        logger.debug('learning rate: {:.6f}'.format(optimizer.param_groups[0]['lr']))
