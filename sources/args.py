
import dataclasses
from dataclasses import dataclass, field
import os
import enums


@dataclass
class RuntimeArguments:
    """Arguments for runtime."""

    do_pre_train: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to pre-train'}
    )

    pre_train_tasks: str = field(
        default=','.join(enums.PRE_TRAIN_TASKS),
        metadata={'help': 'Pre-training tasks in order, split by commas, '
                          'for example (default) {}'.format(','.join(enums.PRE_TRAIN_TASKS))}
    )

    do_fine_tune: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to fine_tune, task can be specific by `--task`'}
    )

    only_test: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to test only'}
    )

    task: str = field(
        default='summarization',
        metadata={'help': 'Downstream task',
                  'choices': enums.ALL_DOWNSTREAM_TASKS}
    )

    trained_vocab: str = field(
        default='../pre_trained/vocabs/',
        metadata={'help': 'Directory of trained vocabs'}
    )

    trained_model: str = field(
        default='../pre_trained/models/all/',
        metadata={'help': 'Directory of trained model'}
    )

    train_from_scratch: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to train from scratch, will ignore `--trained_model`'}
    )

    random_seed: int = field(
        default=42,
        metadata={'help': 'Specific random seed manually for all operations, 0 to disable'}
    )

    n_epoch: int = field(
        default=50,
        metadata={'help': 'Number of data iterations for training'}
    )

    batch_size: int = field(
        default=64,
        metadata={'help': 'Batch size for training on each device'}
    )

    eval_batch_size: int = field(
        default=64,
        metadata={'help': 'Batch size for evaluation on each device'}
    )

    beam_width: int = field(
        default=5,
        metadata={'help': 'Beam width when using beam decoding, 1 to greedy decode'}
    )

    logging_steps: int = field(
        default=100,
        metadata={'help': 'Log training state every n steps'}
    )

    cuda_visible_devices: str = field(
        default=None,
        metadata={'help': 'Visible cuda devices, string formatted, device number divided by \',\', e.g., \'0, 2\', '
                          '\'None\' will use all'}
    )

    fp16: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to use mixed precision'}
    )


@dataclass
class DatasetArguments:
    """Arguments for dataset loading."""

    dataset_root: str = field(
        default='../../dataset/',
        metadata={'help': 'Root of the dataset'}
    )

    train_subset_ratio: float = field(
        default=None,
        metadata={'help': 'Ratio of train subset'}
    )

    pre_train_subset_ratio: float = field(
        default=None,
        metadata={'help': 'Ratio of pre-train subset'}
    )


@dataclass
class SavingArguments:
    """Arguments for saving and loading."""

    model_name: str = field(
        default='default_model',
        metadata={'help': 'Name of the model'}
    )

    dataset_save_dir: str = field(
        default=os.path.join(DatasetArguments.dataset_root, 'dataset_saved'),
        metadata={'help': 'Directory to save and load dataset pickle instance'}
    )

    vocab_save_dir: str = field(
        default=os.path.join(DatasetArguments.dataset_root, 'vocab_saved'),
        metadata={'help': 'Directory to save and load vocab pickle instance'}
    )


@dataclass
class PreprocessingArguments:
    """Arguments for data preprocessing."""

    code_vocab_size: int = field(
        default=50000,
        metadata={'help': 'Maximum size of code vocab'}
    )

    nl_vocab_size: int = field(
        default=30000,
        metadata={'help': 'Maximum size of nl vocab'}
    )

    code_vocab_name: str = field(
        default='code',
        metadata={'help': 'Name of the code vocab'}
    )

    ast_vocab_name: str = field(
        default='ast',
        metadata={'help': 'Name of the ast vocab'}
    )

    nl_vocab_name: str = field(
        default='nl',
        metadata={'help': 'Name of the nl vocab'}
    )

    max_code_len: int = field(
        default=256,
        metadata={'help': 'Maximum length of code sequence'}
    )

    max_ast_len: int = field(
        default=32,
        metadata={'help': 'Maximum length of ast sequence'}
    )

    max_nl_len: int = field(
        default=64,
        metadata={'help': 'Maximum length of the nl sequence'}
    )

    code_tokenize_method: str = field(
        default='bpe',
        metadata={'help': 'Tokenize method of code',
                  'choices': ['word', 'bpe']}
    )

    nl_tokenize_method: str = field(
        default='bpe',
        metadata={'help': 'Tokenize method of nl',
                  'choices': ['word', 'bpe']}
    )

    no_ast: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to eliminate AST from input'}
    )

    no_nl: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to eliminate natural language from input'}
    )


@dataclass
class ModelArguments:
    """Arguments for model related hyper-parameters"""

    d_model: int = field(
        default=768,
        metadata={'help': 'Dimension of the model'}
    )

    d_ff: int = field(
        default=3072,
        metadata={'help': 'Dimension of the feed forward layer'}
    )

    n_head: int = field(
        default=12,
        metadata={'help': 'Number of head of self attention'}
    )

    n_layer: int = field(
        default=12,
        metadata={'help': 'Number of layer'}
    )

    dropout: float = field(
        default=0.1,
        metadata={'help': 'Dropout probability'}
    )


@dataclass
class OptimizerArguments:
    """Arguments for optimizer, early stopping, warmup, grad clipping, label smoothing."""

    learning_rate: float = field(
        default=5e-5,
        metadata={'help': 'Learning rate'}
    )

    lr_decay_rate: float = field(
        default=0,
        metadata={'help': 'Decay ratio for learning rate, 0 to disable'}
    )

    early_stop_patience: int = field(
        default=20,
        metadata={'help': 'Stop training if performance does not improve in n epoch, 0 to disable'}
    )

    warmup_steps: int = field(
        default=1000,
        metadata={'help': 'Warmup steps for optimizer, 0 to disable'}
    )

    grad_clipping_norm: float = field(
        default=1.0,
        metadata={'help': 'Gradient clipping norm, 0 to disable'}
    )

    gradient_accumulation_steps: int = field(
        default=1,
        metadata={'help': 'Gradient accumulation steps, default to 1'}
    )

    label_smoothing: float = field(
        default=0.1,
        metadata={'help': 'Label smoothing ratio, 0 to disable'}
    )


@dataclass
class TaskArguments:
    """Arguments for specific tasks"""

    mass_mask_ratio: float = field(
        default=0.5,
        metadata={'help': 'Ratio between number of masked tokens and number of total tokens, in MASS'}
    )

    summarization_language: str = field(
        default='java',
        metadata={'help': 'Language of the source code in code summarization, also the directory of the dataset dir'}
    )

    completion_max_len: int = field(
        default=32,
        metadata={'help': 'Max length of code to completion'}
    )

    translation_source_language: str = field(
        default='java',
        metadata={'help': 'Source language of the code translation',
                  'choices': ['java', 'c_sharp']}
    )

    translation_target_language: str = field(
        default='c_sharp',
        metadata={'help': 'Target language of the code translation',
                  'choices': ['java', 'c_sharp']}
    )

    search_language: str = field(
        default='java',
        metadata={'help': 'Language of the source code in code search, also the directory of the dataset dir'}
    )

    bug_fix_scale: str = field(
        default='small',
        metadata={'help': 'Scale of the bug fix dataset.',
                  'choices': ['small', 'medium']}
    )


def transfer_arg_name(name):
    return '--' + name.replace('_', '-')


def add_args(parser):
    """Add all arguments to the given parser."""
    for data_container in [RuntimeArguments, DatasetArguments, SavingArguments,
                           PreprocessingArguments, ModelArguments, OptimizerArguments, TaskArguments]:
        group = parser.add_argument_group(data_container.__name__)
        for data_field in dataclasses.fields(data_container):
            if 'action' in data_field.metadata:
                group.add_argument(transfer_arg_name(data_field.name),
                                   default=data_field.default,
                                   **data_field.metadata)
            else:
                group.add_argument(transfer_arg_name(data_field.name),
                                   type=data_field.type,
                                   default=data_field.default,
                                   **data_field.metadata)
