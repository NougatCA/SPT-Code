
"""
参数配置模块

该模块定义了用于机器学习训练流程的各种参数配置类。
使用 dataclass 装饰器来创建参数类，便于管理和维护训练过程中的超参数。

主要包含以下参数类：
1. RuntimeArguments: 运行时参数
2. DatasetArguments: 数据集相关参数
3. SavingArguments: 保存和加载相关参数
4. PreprocessingArguments: 数据预处理参数
5. ModelArguments: 模型结构参数
6. OptimizerArguments: 优化器参数
7. TaskArguments: 特定任务参数

作者: NougatCA
项目: SPT-Code
"""

import dataclasses
from dataclasses import dataclass, field
import os
import enums


@dataclass
class RuntimeArguments:
    """
    运行时参数配置类
    
    定义了训练和测试过程中的运行时配置，包括：
    - 预训练和微调控制
    - 模型加载路径
    - 训练轮数和批次大小
    - GPU设置等
    """

    do_pre_train: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to pre-train'}  # 是否进行预训练
    )

    pre_train_tasks: str = field(
        default=','.join(enums.PRE_TRAIN_TASKS),
        metadata={'help': 'Pre-training tasks in order, split by commas, '  # 预训练任务列表，用逗号分隔
                          'for example (default) {}'.format(','.join(enums.PRE_TRAIN_TASKS))}
    )

    do_fine_tune: bool = field(
        default=True,
        metadata={'action': 'store_true',
                  'help': 'Whether to fine_tune, task can be specific by `--task`'}  # 是否进行微调
    )

    only_test: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to test only'}  # 是否只进行测试
    )

    task: str = field(
        default='search',
        metadata={'help': 'Downstream task',  # 下游任务类型
                  'choices': enums.ALL_DOWNSTREAM_TASKS}
    )

    trained_vocab: str = field(
        default='../pre_trained/vocabs/',
        metadata={'help': 'Directory of trained vocabs'}  # 预训练词汇表目录
    )

    trained_model: str = field(
        default='../pre_trained/models/all/',
        metadata={'help': 'Directory of trained model'}  # 预训练模型目录
    )

    train_from_scratch: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to train from scratch, will ignore `--trained_model`'}  # 是否从零开始训练
    )

    random_seed: int = field(
        default=42,
        metadata={'help': 'Specific random seed manually for all operations, 0 to disable'}  # 随机种子设置
    )

    n_epoch: int = field(
        default=50,
        metadata={'help': 'Number of data iterations for training'}  # 训练轮数
    )

    batch_size: int = field(
        default=16,
        metadata={'help': 'Batch size for training on each device'}  # 每个设备的训练批次大小
    )

    eval_batch_size: int = field(
        default=16,
        metadata={'help': 'Batch size for evaluation on each device'}  # 每个设备的评估批次大小
    )

    beam_width: int = field(
        default=5,
        metadata={'help': 'Beam width when using beam decoding, 1 to greedy decode'}  # beam搜索宽度
    )

    logging_steps: int = field(
        default=100,
        metadata={'help': 'Log training state every n steps'}  # 日志记录间隔步数
    )

    cuda_visible_devices: str = field(
        default=None,
        metadata={'help': 'Visible cuda devices, string formatted, device number divided by \',\', e.g., \'0, 2\', '
                          '\'None\' will use all'}  # 可见的CUDA设备
    )

    fp16: bool = field(
        default=True,
        metadata={'action': 'store_true',
                  'help': 'Whether to use mixed precision'}  # 是否使用混合精度训练
    )


@dataclass
class DatasetArguments:
    """
    数据集参数配置类
    
    定义了数据集相关的配置参数，包括：
    - 数据集根目录
    - 训练子集比例
    - 预训练子集比例
    """

    dataset_root: str = field(
        default='../../dataset/',
        metadata={'help': 'Root of the dataset'}  # 数据集根目录
    )

    train_subset_ratio: float = field(
        default=None,
        metadata={'help': 'Ratio of train subset'}  # 训练子集比例
    )

    pre_train_subset_ratio: float = field(
        default=None,
        metadata={'help': 'Ratio of pre-train subset'}  # 预训练子集比例
    )


@dataclass
class SavingArguments:
    """
    保存和加载参数配置类
    
    定义了模型、数据集和词汇表的保存加载路径配置，包括：
    - 模型名称
    - 数据集保存目录
    - 词汇表保存目录
    """

    model_name: str = field(
        default='default_model',
        metadata={'help': 'Name of the model'}  # 模型名称
    )

    dataset_save_dir: str = field(
        default=os.path.join(DatasetArguments.dataset_root, 'dataset_saved'),
        metadata={'help': 'Directory to save and load dataset pickle instance'}  # 数据集保存目录
    )

    vocab_save_dir: str = field(
        default=os.path.join(DatasetArguments.dataset_root, 'vocab_saved'),
        metadata={'help': 'Directory to save and load vocab pickle instance'}  # 词汇表保存目录
    )


@dataclass
class PreprocessingArguments:
    """
    数据预处理参数配置类
    
    定义了数据预处理相关的参数，包括：
    - 词汇表大小和名称设置
    - 序列最大长度限制
    - 分词方法选择
    - 输入组件控制（AST、自然语言）
    """

    code_vocab_size: int = field(
        default=50000,
        metadata={'help': 'Maximum size of code vocab'}  # 代码词汇表最大大小
    )

    nl_vocab_size: int = field(
        default=30000,
        metadata={'help': 'Maximum size of nl vocab'}  # 自然语言词汇表最大大小
    )

    code_vocab_name: str = field(
        default='code',
        metadata={'help': 'Name of the code vocab'}  # 代码词汇表名称
    )

    ast_vocab_name: str = field(
        default='ast',
        metadata={'help': 'Name of the ast vocab'}  # AST词汇表名称
    )

    nl_vocab_name: str = field(
        default='nl',
        metadata={'help': 'Name of the nl vocab'}  # 自然语言词汇表名称
    )

    max_code_len: int = field(
        default=256,
        metadata={'help': 'Maximum length of code sequence'}  # 代码序列最大长度
    )

    max_ast_len: int = field(
        default=32,
        metadata={'help': 'Maximum length of ast sequence'}  # AST序列最大长度
    )

    max_nl_len: int = field(
        default=64,
        metadata={'help': 'Maximum length of the nl sequence'}  # 自然语言序列最大长度
    )

    code_tokenize_method: str = field(
        default='bpe',
        metadata={'help': 'Tokenize method of code',  # 代码分词方法
                  'choices': ['word', 'bpe']}
    )

    nl_tokenize_method: str = field(
        default='bpe',
        metadata={'help': 'Tokenize method of nl',  # 自然语言分词方法
                  'choices': ['word', 'bpe']}
    )

    no_ast: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to eliminate AST from input'}  # 是否从输入中移除AST
    )

    no_nl: bool = field(
        default=False,
        metadata={'action': 'store_true',
                  'help': 'Whether to eliminate natural language from input'}  # 是否从输入中移除自然语言
    )


@dataclass
class ModelArguments:
    """
    模型结构参数配置类
    
    定义了Transformer模型的结构超参数，包括：
    - 模型维度
    - 前馈网络维度
    - 注意力头数
    - 层数
    - Dropout概率
    """

    d_model: int = field(
        default=768,
        metadata={'help': 'Dimension of the model'}  # 模型维度
    )

    d_ff: int = field(
        default=3072,
        metadata={'help': 'Dimension of the feed forward layer'}  # 前馈层维度
    )

    n_head: int = field(
        default=12,
        metadata={'help': 'Number of head of self attention'}  # 自注意力头数
    )

    n_layer: int = field(
        default=12,
        metadata={'help': 'Number of layer'}  # 层数
    )

    dropout: float = field(
        default=0.1,
        metadata={'help': 'Dropout probability'}  # Dropout概率
    )


@dataclass
class OptimizerArguments:
    """
    优化器参数配置类
    
    定义了优化器相关的超参数，包括：
    - 学习率和衰减策略
    - 早停机制
    - 预热步数
    - 梯度裁剪
    - 梯度累积
    - 标签平滑
    """

    learning_rate: float = field(
        default=5e-5,
        metadata={'help': 'Learning rate'}  # 学习率
    )

    lr_decay_rate: float = field(
        default=0,
        metadata={'help': 'Decay ratio for learning rate, 0 to disable'}  # 学习率衰减比例
    )

    early_stop_patience: int = field(
        default=20,
        metadata={'help': 'Stop training if performance does not improve in n epoch, 0 to disable'}  # 早停耐心值
    )

    warmup_steps: int = field(
        default=1000,
        metadata={'help': 'Warmup steps for optimizer, 0 to disable'}  # 优化器预热步数
    )

    grad_clipping_norm: float = field(
        default=1.0,
        metadata={'help': 'Gradient clipping norm, 0 to disable'}  # 梯度裁剪范数
    )

    gradient_accumulation_steps: int = field(
        default=1,
        metadata={'help': 'Gradient accumulation steps, default to 1'}  # 梯度累积步数
    )

    label_smoothing: float = field(
        default=0.1,
        metadata={'help': 'Label smoothing ratio, 0 to disable'}  # 标签平滑比例
    )


@dataclass
class TaskArguments:
    """
    特定任务参数配置类
    
    定义了不同下游任务的特定参数，包括：
    - MASS任务的掩码比例
    - 代码摘要任务的编程语言
    - 代码补全的最大长度
    - 代码翻译的源语言和目标语言
    - 代码搜索的编程语言
    - Bug修复数据集规模
    """

    mass_mask_ratio: float = field(
        default=0.5,
        metadata={'help': 'Ratio between number of masked tokens and number of total tokens, in MASS'}  # MASS任务掩码比例
    )

    summarization_language: str = field(
        default='java',
        metadata={'help': 'Language of the source code in code summarization, also the directory of the dataset dir'}  # 代码摘要任务的编程语言
    )

    completion_max_len: int = field(
        default=32,
        metadata={'help': 'Max length of code to completion'}  # 代码补全的最大长度
    )

    translation_source_language: str = field(
        default='java',
        metadata={'help': 'Source language of the code translation',  # 代码翻译的源语言
                  'choices': ['java', 'c_sharp']}
    )

    translation_target_language: str = field(
        default='c_sharp',
        metadata={'help': 'Target language of the code translation',  # 代码翻译的目标语言
                  'choices': ['java', 'c_sharp']}
    )

    search_language: str = field(
        default='java',
        metadata={'help': 'Language of the source code in code search, also the directory of the dataset dir'}  # 代码搜索的编程语言
    )

    bug_fix_scale: str = field(
        default='small',
        metadata={'help': 'Scale of the bug fix dataset.',  # Bug修复数据集规模
                  'choices': ['small', 'medium']}
    )


def transfer_arg_name(name):
    """
    转换参数名称格式
    
    将下划线格式的参数名转换为命令行格式（添加--前缀，下划线转横线）
    
    Args:
        name (str): 原始参数名（下划线格式）
        
    Returns:
        str: 转换后的命令行参数名格式
        
    Example:
        >>> transfer_arg_name('batch_size')
        '--batch-size'
    """
    return '--' + name.replace('_', '-')


def add_args(parser):
    """
    向解析器添加所有参数
    
    遍历所有参数配置类，将每个类中定义的字段作为命令行参数添加到ArgumentParser中。
    根据metadata中的action字段决定参数类型的处理方式。
    
    Args:
        parser (ArgumentParser): 命令行参数解析器对象
        
    Note:
        - 为每个参数类创建一个参数组
        - 根据是否包含'action'字段来决定参数添加方式
        - 'action'字段存在时使用store_true类型的布尔参数
        - 'action'字段不存在时使用字段类型作为参数类型
    """
    # 遍历所有参数配置类
    for data_container in [RuntimeArguments, DatasetArguments, SavingArguments,
                           PreprocessingArguments, ModelArguments, OptimizerArguments, TaskArguments]:
        # 为每个参数类创建参数组
        group = parser.add_argument_group(data_container.__name__)
        
        # 遍历参数类中的所有字段
        for data_field in dataclasses.fields(data_container):
            # 根据metadata中是否包含action来决定参数添加方式
            if 'action' in data_field.metadata:
                # 布尔类型参数（store_true action）
                group.add_argument(transfer_arg_name(data_field.name),
                                   default=data_field.default,
                                   **data_field.metadata)
            else:
                # 普通类型参数
                group.add_argument(transfer_arg_name(data_field.name),
                                   type=data_field.type,
                                   default=data_field.default,
                                   **data_field.metadata)
