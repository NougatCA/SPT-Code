
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

    def set_task(self, task):
        self.task = task
