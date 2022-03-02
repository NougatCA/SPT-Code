# SPT-Code

## Requirements

### Minimize requirements

The list of minimize requirements can be found in `requirements.txt`.

### Additional requirements

If you need to reprocess the raw dataset, or use your own dataset,
then you will also need to install the following packages.
```
tree_sitter==0.19.0
antlr4-python3-runtime==4.9.2
```
Besides, `antlr4` need to be installed,
[installation guidance here](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md).

If you encounter errors about `my-languages.so` when preprocessing the dataset, 
please run `sources/data/asts/build_lib.py` first.

## Datasets and Tokenizers

We provide pre-processed datasets, saved as pickle binary files, 
which can be loaded directly as instances.

The pre-processed datasets can be downloaded here: ([OneDrive](https://1drv.ms/u/s!Aj4XBdlu8BS0geoX0UgaslHdGvUCpg?e=sjBC6J), [iCloud](https://www.icloud.com.cn/iclouddrive/0158Oqc01mJDU9hOTsdsyoFDw#dataset), [GoogleDrive](https://drive.google.com/file/d/1Uf78WZYd_OqsV46j2Z7zWqtgmiDAFJb8/view?usp=sharing)).
Put the downloaded dataset pickle file into `{dataset_root}/dataset_saved/` (default to`.../dataset/dataset_saved`), 
the program will automatically detect and use it.

It is also possible to use a custom dataset, 
simply by placing it in the specified location according to the relevant settings in the source code, 
or by modifying the corresponding dataset loading script in the source code. 
The dataset loading code is located in the `sources/data/data.py` and `sources/data/data_utils.py` files.

##  Pre-trained Tokenizers and Models

Custom tokenizers (we call "vocab") can be downloaded here: ([OneDrive](https://1drv.ms/u/s!Aj4XBdlu8BS0geoV78e2KLC41sfasw?e=kfukTw), [iCloud](https://www.icloud.com.cn/iclouddrive/033gKQZigREGSYzRef-2yP6Bg#pre%5Ftrained), [Google Drive](https://drive.google.com/file/d/1PhVf5u8_uq5Tsl-OIvOGpqjA2y7D-9Dr/view?usp=sharing)). Extract it in a certain directory. 
Specific the argument `trained_vocab` of `main.py` 
where the tokenizers are located or put it in `{dataset_root}/vocab_saved` (default to`.../dataset/vocab_saved`).

You may pre-train SPT-Code by yourself. We also provide pre-trained models available [here](https://1drv.ms/u/s!Aj4XBdlu8BS0geoV78e2KLC41sfasw?e=kfukTw).
Extract and put it in a directory, then specific the argument `trained_model` like tokenizers before.

## Runs

Run `main.py` to start pre-train, fine-tune or test. 
All arguments are located in `args.py`, specific whatever you need.

Some example scripts are as following.
```shell
# pre-training
python main.py \
--do-pre-train \
--pre-train-tasks cap,mass,mng \
--batch-size 64 \
--eval-batch-size 64 \
--cuda-visible-devices 0,1,2,3 \
--fp16 \
--model-name pre_train

# summarization on pre-trained model and vocab
python main.py \
--do-fine-tune \
--task summarization \
--summarization-language java \
--model-name summarization_java \
--trained_vocab '../pre_trained/vocabs/' \
--trained_model '../pre_trained/models/all/'

# bug fixing without pre-training
python main.py \
--do-fine-tune \
--train-from-scratch \
--task bug_fix \
--bug_fix_scale medium

# only test on translation
python main.py \
--only-test \
--task translation \
--translation-source-language java \
--translation-target-language c_sharp \
--trained_vocab '../pre_trained/vocabs/' \
--trained_model '../outputs/translation_java_c_sharp_20210826_052653/models/'
```
