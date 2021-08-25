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


class SearchValidCallBack(TrainerCallback):

    def __init__(self,
                 codebase_dataloader: torch.utils.data.dataloader.DataLoader,
                 eval_dataloader: torch.utils.data.dataloader.DataLoader,
                 early_stop_patience):
        self.codebase_dataloader = codebase_dataloader
        self.eval_dataloader = eval_dataloader
        self.early_stopping = EarlyStopping(patience=early_stop_patience, higher_better=True)

    def on_epoch_end(self,
                     args: TrainingArguments,
                     state: TrainerState,
                     control: TrainerControl,
                     model: BartForClassificationAndGeneration,
                     eval_dataloader: torch.utils.data.dataloader.DataLoader,
                     **kwargs):
        logger.info("***** Running evaluation *****")
        logger.info("  Num queries = %d", len(self.eval_dataloader.dataset))
        logger.info("  Num codes = %d", len(self.codebase_dataloader.dataset))
        logger.info("  Batch size = %d", args.eval_batch_size)

        results = model.evaluate_search(query_dataloader=self.eval_dataloader,
                                        codebase_dataloader=self.codebase_dataloader,
                                        metrics_prefix='valid')
        logger.info(results)
        mrr = results['valid_mrr']
        self.early_stopping(score=mrr, model=None, epoch=state.epoch)

        if self.early_stopping.refreshed:
            control.should_save = True
        if self.early_stopping.early_stop:
            control.should_training_stop = True
