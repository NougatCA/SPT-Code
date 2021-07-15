
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.dataset import Dataset
from transformers import Seq2SeqTrainer, Trainer

import argparse
from typing import Optional

from data.data_collator import collate_fn


class CodeTrainer(Seq2SeqTrainer):

    def __init__(self, main_args: argparse.Namespace, code_vocab, ast_vocab, nl_vocab, task, **kwargs):
        super(CodeTrainer, self).__init__(**kwargs)
        self.main_args = main_args
        self.code_vocab = code_vocab
        self.ast_vocab = ast_vocab
        self.nl_vocab = nl_vocab
        self.task = task

    def get_train_dataloader(self) -> DataLoader:
        """
        Returns the training :class:`~torch.utils.data.DataLoader`.

        Will use no sampler if :obj:`self.train_dataset` does not implement :obj:`__len__`, a random sampler (adapted
        to distributed training if necessary) otherwise.

        Subclass and override this method if you want to inject some custom behavior.
        """

        return DataLoader(dataset=self.train_dataset,
                          batch_size=self.main_args.batch_size,
                          shuffle=True,
                          collate_fn=lambda batch: collate_fn(batch,
                                                              args=self.main_args,
                                                              task=self.task,
                                                              code_vocab=self.code_vocab,
                                                              nl_vocab=self.nl_vocab,
                                                              ast_vocab=self.ast_vocab))

    def get_eval_dataloader(self, eval_dataset: Optional[Dataset] = None) -> DataLoader:
        if eval_dataset:
            self.eval_dataset = eval_dataset
        return DataLoader(dataset=self.eval_dataset,
                          batch_size=self.main_args.eval_batch_size,
                          collate_fn=lambda batch: collate_fn(batch,
                                                              args=self.main_args,
                                                              task=self.task,
                                                              code_vocab=self.code_vocab,
                                                              nl_vocab=self.nl_vocab,
                                                              ast_vocab=self.ast_vocab))

    def get_test_dataloader(self, test_dataset: Dataset) -> DataLoader:
        return DataLoader(dataset=test_dataset,
                          batch_size=self.main_args.eval_batch_size,
                          collate_fn=lambda batch: collate_fn(batch,
                                                              args=self.main_args,
                                                              task=self.task,
                                                              code_vocab=self.code_vocab,
                                                              nl_vocab=self.nl_vocab,
                                                              ast_vocab=self.ast_vocab))

    def set_task(self, task):
        self.task = task


class CodeCLSTrainer(Trainer):

    def __init__(self, main_args: argparse.Namespace, code_vocab, ast_vocab, nl_vocab, task, **kwargs):
        super(CodeCLSTrainer, self).__init__(**kwargs)
        self.main_args = main_args
        self.code_vocab = code_vocab
        self.ast_vocab = ast_vocab
        self.nl_vocab = nl_vocab
        self.task = task

    def get_train_dataloader(self) -> DataLoader:
        """
        Returns the training :class:`~torch.utils.data.DataLoader`.

        Will use no sampler if :obj:`self.train_dataset` does not implement :obj:`__len__`, a random sampler (adapted
        to distributed training if necessary) otherwise.

        Subclass and override this method if you want to inject some custom behavior.
        """

        return DataLoader(dataset=self.train_dataset,
                          batch_size=self.main_args.batch_size,
                          shuffle=True,
                          collate_fn=lambda batch: collate_fn(batch,
                                                              args=self.main_args,
                                                              task=self.task,
                                                              code_vocab=self.code_vocab,
                                                              nl_vocab=self.nl_vocab,
                                                              ast_vocab=self.ast_vocab))

    def get_eval_dataloader(self, eval_dataset: Optional[Dataset] = None) -> DataLoader:
        if eval_dataset:
            self.eval_dataset = eval_dataset
        return DataLoader(dataset=self.eval_dataset,
                          batch_size=self.main_args.eval_batch_size,
                          collate_fn=lambda batch: collate_fn(batch,
                                                              args=self.main_args,
                                                              task=self.task,
                                                              code_vocab=self.code_vocab,
                                                              nl_vocab=self.nl_vocab,
                                                              ast_vocab=self.ast_vocab))

    def get_test_dataloader(self, test_dataset: Dataset) -> DataLoader:
        return DataLoader(dataset=test_dataset,
                          batch_size=self.main_args.eval_batch_size,
                          collate_fn=lambda batch: collate_fn(batch,
                                                              args=self.main_args,
                                                              task=self.task,
                                                              code_vocab=self.code_vocab,
                                                              nl_vocab=self.nl_vocab,
                                                              ast_vocab=self.ast_vocab))

    def set_task(self, task):
        self.task = task
