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

    def on_epoch_begin(self,
                       args: TrainingArguments,
                       state: TrainerState,
                       control: TrainerControl,
                       **kwargs):
        self.epoch_timer.reset()
        logger.debug(f'Start epoch {state.epoch}')

    def on_epoch_end(self,
                     args: TrainingArguments,
                     state: TrainerState,
                     control: TrainerControl,
                     optimizer: torch.optim.Optimizer,
                     **kwargs):
        logger.debug('Epoch {} finished, time: {:.2f}s'.format(state.epoch, self.epoch_timer.time()))
        logger.debug('learning rate: {:.6f}'.format(optimizer.param_groups[0]['lr']))

    def on_evaluate(self,
                    args: TrainingArguments,
                    state: TrainerState,
                    control: TrainerControl,
                    metrics: Dict[str, float],
                    **kwargs):
        logger.debug(f'Evaluation after epoch {state.epoch} finished')
        for metric, value in metrics.items():
            logger.debug(f'{metric}: {value}')


class SearchValidCallBack(TrainerCallback):

    def __init__(self, codebase_dataloader: torch.utils.data.dataloader.DataLoader, early_stop_patience):
        self.codebase_dataloader = codebase_dataloader
        self.early_stopping = EarlyStopping(patience=early_stop_patience, higher_better=True)

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

        results = model.evaluate_search(query_dataloader=eval_dataloader,
                                        codebase_dataloader=self.codebase_dataloader,
                                        metrics_prefix='valid')

        mrr = results['valid_mrr']
        self.early_stopping(score=mrr, model=None, epoch=state.epoch)

        if self.early_stopping.refreshed:
            control.should_save = True
        if self.early_stopping.early_stop:
            control.should_training_stop = True
