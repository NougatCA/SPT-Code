import torch
from transformers import TrainerCallback, TrainingArguments, TrainerState, TrainerControl

import logging

from models.bart import BartForClassificationAndGeneration
from .timer import Timer
import enums


logger = logging.getLogger(__name__)


class LogStateCallBack(TrainerCallback):

    epoch_timer = Timer()

    def on_epoch_begin(self,
                       args: TrainingArguments,
                       state: TrainerState,
                       control: TrainerControl,
                       **kwargs):
        self.epoch_timer.reset()

    def on_epoch_end(self,
                     args: TrainingArguments,
                     state: TrainerState,
                     control: TrainerControl,
                     optimizer: torch.optim.Optimizer,
                     **kwargs):
        logger.debug('Epoch {} finished, time: {:.2f}s'.format(state.epoch, self.epoch_timer.time()))
        logger.debug('learning rate: {:.6f}'.format(optimizer.param_groups[0]['lr']))


class SearchValidCallBack(TrainerCallback):

    def __init__(self, codebase_dataloader: torch.utils.data.dataloader.DataLoader):
        self.codebase_dataloader = codebase_dataloader

    def on_epoch_end(self,
                     args: TrainingArguments,
                     state: TrainerState,
                     control: TrainerControl,
                     model: BartForClassificationAndGeneration,
                     eval_dataloader: torch.utils.data.dataloader.DataLoader,
                     **kwargs):
        logger.info("***** Running evaluation *****")
        logger.info("  Num queries = %d", len(eval_dataloader.dataset))
        logger.info("  Num codes = %d", len(self.codebase_dataloader.dataset))
        logger.info("  Batch size = %d", args.eval_batch_size)

