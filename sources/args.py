
import dataclasses
from dataclasses import dataclass, field
import time
import os


@dataclass
class RuntimeArguments:
    """Arguments for runtime."""

    random_seed: int = field(
        default=42,
        metadata={'help': 'Specific random seed manually for all operations, 0 to disable'}
    )

    n_epoch: int = field(
        default=5,
        metadata={'help': 'Number of data iterations for training'}
    )

    pre_train_n_epoch: int = field(
        default=1,
        metadata={'help': 'Number of data iterations for pre-training on each task'}
    )

    batch_size: int = field(
        default=128,
        metadata={'help': 'Batch size for training on each device'}
    )

    eval_batch_size: int = field(
        default=256,
        metadata={'help': 'Batch size for evaluation on each device'}
    )

    beam_width: int = field(
        default=5,
        metadata={'help': 'Beam width when using beam decoding, 1 to greedy decode'}
    )

    log_state_every: int = field(
        default=100,
        metadata={'help': 'Log training state to log file every n files'}
    )

    cuda_visible_devices: str = field(
        default=None,
        metadata={'help': 'Visible cuda devices, string formatted, device number divided by \',\', e.g., \'0, 2\', '
                          '\'None\' will use all'}
    )


@dataclass
class DatasetArguments:
    """Arguments for dataset loading."""

    dataset_root: str = field(
        default='../../dataset/',
        metadata={'help': 'Root of the dataset'}
    )


@dataclass
class SavingArguments:
    """Arguments for saving and loading."""

    model_name: str = field(
        default='default_model',
        metadata={'help': 'Name of the model'}
    )

    output_root: str = field(
        default='../outputs/{}_{}'.format(model_name.default, time.strftime('%Y%m%d_%H%M%S', time.localtime())),
        metadata={'help': 'Root directory for the output of this run'}
    )

    pre_train_output_root: str = field(
        default=os.path.join(output_root.default, 'pre_train'),
        metadata={'help': 'Root for outputs during pre-training'}
    )

    checkpoint_root: str = field(
        default=os.path.join(output_root.default, 'checkpoints'),
        metadata={'help': 'Root for saving checkpoints'}
    )

    dataset_save_dir: str = field(
        default=os.path.join(DatasetArguments.dataset_root, 'saved'),
        metadata={'help': 'Directory to save and load dataset pickle instance'}
    )

    model_root: str = field(
        default=os.path.join(output_root.default, 'models'),
        metadata={'help': 'Root for saving models'}
    )

    vocab_root: str = field(
        default=os.path.join(output_root.default, 'vocabs'),
        metadata={'help': 'Root for saving vocabs'}
    )

    tensor_board_root: str = field(
        default=os.path.join(output_root.default, 'runs'),
        metadata={'help': 'Directory for tensor board logging'}
    )

    tensor_board_logging_steps: int = field(
        default=500,
        metadata={'help': 'Log to tensor board every this number of steps'}
    )


@dataclass
class PreprocessingArguments:
    """Arguments for data preprocessing."""

    code_vocab_size: int = field(
        default=30000,
        metadata={'help': 'Maximum size of code vocab'}
    )

    nl_vocab_size: int = field(
        default=20000,
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
        default=200,
        metadata={'help': 'Maximum length of code sequence'}
    )

    max_ast_len: int = field(
        default=30,
        metadata={'help': 'Maximum length of ast sequence'}
    )

    max_nl_len: int = field(
        default=50,
        metadata={'help': 'Maximum length of the nl sequence'}
    )

    code_tokenize_method: str = field(
        default='word',
        metadata={'help': 'Tokenize method of code',
                  'choices': ['word', 'bpe']}
    )

    nl_tokenize_method: str = field(
        default='word',
        metadata={'help': 'Tokenize method of nl',
                  'choices': ['word', 'bpe']}
    )


@dataclass
class ModelArguments:
    """Arguments for model related hyper-parameters"""

    d_model: int = field(
        default=512,
        metadata={'help': 'Dimension of the model'}
    )

    d_ff: int = field(
        default=2048,
        metadata={'help': 'Dimension of the feed forward layer'}
    )

    n_head: int = field(
        default=8,
        metadata={'help': 'Number of head of self attention'}
    )

    n_layer: int = field(
        default=6,
        metadata={'help': 'Number of layer'}
    )

    dropout: float = field(
        default=0.1,
        metadata={'help': 'Dropout probability'}
    )

    activate_function: str = field(
        default='gelu',
        metadata={'help': 'Activate function of the model',
                  'choices': ['gelu', 'relu', 'silu', 'gelu_new']}
    )


@dataclass
class OptimizerArguments:
    """Arguments for optimizer, early stopping, warmup, grad clipping, label smoothing."""

    learning_rate: float = field(
        default=3e-4,
        metadata={'help': 'Learning rate'}
    )

    lr_decay_rate: float = field(
        default=0,
        metadata={'help': 'Decay ratio for learning rate, 0 to disable'}
    )

    early_stop_patience: int = field(
        default=10,
        metadata={'help': 'Stop training if performance does not improve in n epoch, 0 to disable'}
    )

    warmup_steps: int = field(
        default=2000,
        metadata={'help': 'Warmup steps for optimizer, 0 to disable'}
    )

    grad_clipping_norm: float = field(
        default=1.0,
        metadata={'help': 'Gradient clipping norm, 0 to disable'}
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
        default='ruby',
        metadata={'help': 'Language of the source code in code search, also the directory of the dataset dir'}
    )


def transfer_arg_name(name):
    return '--' + name.replace('_', '-')


def add_args(parser):
    """Add all arguments to the given parser."""
    for data_container in [RuntimeArguments, DatasetArguments, SavingArguments,
                           PreprocessingArguments, ModelArguments, OptimizerArguments, TaskArguments]:
        group = parser.add_argument_group(data_container.__name__)
        for data_field in dataclasses.fields(data_container):
            group.add_argument(transfer_arg_name(data_field.name),
                               type=data_field.type,
                               default=data_field.default,
                               **data_field.metadata)
