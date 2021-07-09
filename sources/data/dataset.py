from torch.utils.data.dataset import Dataset

import os
import random
import logging

import vars
from .data_utils import load_dataset_from_dir, load_lines, parse_for_summarization, parse_for_translation

logger = logging.getLogger(__name__)


class CodeDataset(Dataset):

    def __init__(self, args, mode, task=None, language=None, split=None):
        """
        Initialization definition.

        Args:
            args (argparse.Namespace): Arguments
            mode (str): Running mode, ``pre_train`` or ``fine_tune``
            task (str): Dataset mode, support pre-training tasks: ['cap', 'ncp', 'mnp'],
                and downstream fine-tuning task: ['summarization', 'translation'],
                future support ['completion', 'search', 'clone', 'summarization', 'refinement']
            language (str): Only for downstream fine-tuning
            split (str): Only for downstream fine-tuning, support ['train', 'valid', 'test']

        """
        super(CodeDataset, self).__init__()
        self.task = task
        self.mode = mode

        # dataset dir for files, all files in this dir meeting the filename will be used as dataset files
        self.dataset_dir = os.path.join(args.dataset_root, self.mode)

        # load pre-training dataset
        if self.mode == 'pre_train':
            self.languages, self.lang_n_line, self.sources, self.codes, self.asts, self.names = load_dataset_from_dir(
                dataset_dir=self.dataset_dir, replace_method_name=self.task == vars.TASK_METHOD_NAME_PREDICTION)
            self.size = len(self.codes)
        # load fine-tuning dataset
        else:
            assert split
            self.dataset_dir = os.path.join(self.dataset_dir, task)
            # code summarization
            if task == vars.TASK_SUMMARIZATION:
                assert language, '\'Language\' must be specific if downstream task is code summarization'
                self.dataset_dir = os.path.join(self.dataset_dir, language, split)

                self.source_path = os.path.join(self.dataset_dir, args.source_filename)
                self.code_path = os.path.join(self.dataset_dir, args.code_filename)
                self.nl_path = os.path.join(self.dataset_dir, args.nl_filename)

                self.codes, self.asts, self.names, self.nls = parse_for_summarization(source_path=self.source_path,
                                                                                      code_path=self.code_path,
                                                                                      nl_path=self.nl_path,
                                                                                      lang=language)

                assert len(self.codes) == len(self.asts) == len(self.names) == len(self.nls)
                self.size = len(self.codes)
            # code translation
            elif task == vars.TASK_TRANSLATION:
                java_path = f'{split}.java-cs.txt.java'
                c_sharp_path = f'{split}.java-cs.txt.cs'
                if args.translation_source_language == args.translation_target_language:
                    logger.warning(f'Source language and target language for code translation are '
                                   f'both {args.translation_source_language}')
                source_path = os.path.join(self.dataset_dir,
                                           c_sharp_path if args.translation_source_language == 'c_sharp' else java_path)
                target_path = os.path.join(self.dataset_dir,
                                           c_sharp_path if args.translation_target_language == 'c_sharp' else java_path)
                self.codes, self.asts, self.names, self.targets = parse_for_translation(
                    source_path=source_path,
                    source_lang=args.translation_source_language,
                    target_path=target_path,
                    target_lang=args.translation_target_language)

                assert len(self.codes) == len(self.asts) == len(self.names) == len(self.targets)
                self.size = len(self.codes)

            elif task == vars.TASK_SEARCH:
                pass

    def __getitem__(self, index):
        # cap
        if self.task == vars.TASK_CODE_AST_PREDICTION:
            is_ast = random.random() < 0.5
            if is_ast:
                return self.codes[index], self.asts[index], self.names[index], 1
            else:
                other_ast = self.asts[random.randint(0, self.size - 1)]
                while other_ast == self.asts[index]:
                    other_ast = self.asts[random.randint(0, self.size - 1)]
                return self.codes[index], other_ast, self.names[index], 0
        # ncp
        elif self.task == vars.TASK_NEXT_CODE_PREDICTION:
            return self.languages[index], self.sources[index], self.names[index]
        # mnp
        elif self.task == vars.TASK_METHOD_NAME_PREDICTION:
            return self.codes[index], self.asts[index], self.names[index]
        # summarization
        elif self.task == vars.TASK_SUMMARIZATION:
            return self.codes[index], self.asts[index], self.names[index], self.nls[index]
        # translation
        elif self.task == vars.TASK_TRANSLATION:
            return self.codes[index], self.asts[index], self.names[index], self.targets[index]
        # search
        elif self.task == vars.TASK_SEARCH:
            pass

    def __len__(self):
        return self.size

    def set_task(self, task):
        self.task = task
