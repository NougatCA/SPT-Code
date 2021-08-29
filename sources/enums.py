# training mode
TRAINING_MODE_PRE_TRAIN = 'pre_train'
TRAINING_MODE_FINE_TUNE = 'fine_tune'

# pre-training task names
TASK_CODE_AST_PREDICTION = 'cap'
TASK_MASS = 'mass'
TASK_METHOD_NAME_PREDICTION = 'mng'

PRE_TRAIN_TASKS = [
    TASK_CODE_AST_PREDICTION,
    TASK_MASS,
    TASK_METHOD_NAME_PREDICTION
]

# downstream task names
TASK_SUMMARIZATION = 'summarization'
TASK_TRANSLATION = 'translation'
TASK_SEARCH = 'search'
TASK_CLONE_DETECTION = 'clone'
TASK_COMPLETION = 'completion'
TASK_BUG_FIX = 'bug_fix'

ALL_DOWNSTREAM_TASKS = [
    TASK_SUMMARIZATION,
    TASK_TRANSLATION,
    TASK_SEARCH,
    TASK_CLONE_DETECTION,
    TASK_COMPLETION,
    TASK_BUG_FIX
]

# programming language
LANG_JAVA = 'java'
LANG_PYTHON = 'python'
LANG_GO = 'go'
LANG_PHP = 'php'
LANG_JAVASCRIPT = 'javascript'
LANG_RUBY = 'ruby'
LANG_C_SHARP = 'c_sharp'

# BART model mode
MODEL_MODE_CLS = 'bart_cls'
MODEL_MODE_GEN = 'bart_gen'
MODEL_MODE_SEARCH = 'bart_search'
