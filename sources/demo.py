
# from tokenizers import Tokenizer
# from tokenizers.models import BPE, WordLevel
# from tokenizers.trainers import BpeTrainer, WordLevelTrainer
# from tokenizers.pre_tokenizers import Whitespace
# from tokenizers import normalizers
# from tokenizers.normalizers import NFD, StripAccents, Strip, Lowercase
# from tokenizers.processors import TemplateProcessing, BertProcessing
#
# import os

# special vocabulary symbols
# PAD_TOKEN = '[PAD]'     # padding token
# SOS_TOKEN = '[SOS]'     # start of sequence
# EOS_TOKEN = '[EOS]'     # end of sequence
# UNK_TOKEN = '[UNK]'     # unknown token
# MSK_TOKEN = '[MSK]'     # mask token
# SEP_TOKEN = '[SEP]'     # sentence separator token
# CLS_TOKEN = '[CLS]'     # classification placeholder
#
# # default special symbols, if need additional symbols, use init parameter 'additional_special_symbols'
# START_VOCAB = [PAD_TOKEN, SOS_TOKEN, EOS_TOKEN, UNK_TOKEN, MSK_TOKEN, SEP_TOKEN, CLS_TOKEN]
#
# method = 'bpe'
#
# if method == 'word':
#     tokenize_class = WordLevel
#     trainer_class = WordLevelTrainer
# else:
#     tokenize_class = BPE
#     trainer_class = BpeTrainer
#
# tokenizer = Tokenizer(tokenize_class(unk_token='[UNK]'))
# trainer = trainer_class(special_tokens=START_VOCAB, vocab_size=30000, show_progress=True)
# tokenizer.__setattr__('pre_tokenizer', Whitespace())
#
# # train
# files = ['../../dataset/java/train/token.code']
# ignore_case = True
# if ignore_case:
#     normalizer = normalizers.Sequence([NFD(), StripAccents(), Strip(), Lowercase()])
# else:
#     normalizer = normalizers.Sequence([NFD(), StripAccents(), Strip()])
# tokenizer.__setattr__('normalizer', normalizer)
#
# tokenizer.train(files=files, trainer=trainer)
#
# vocab_name = 'test'
# vocab_dir = os.path.join('test_outputs', vocab_name)
# if not os.path.exists(vocab_dir) or not os.path.isdir(vocab_dir):
#     os.makedirs(vocab_dir)
#
# # save pickle file for whole instance
# # save tokenizer
# tokenizer.save(os.path.join(vocab_dir, '{}_tokenizer.json'.format(vocab_name)))
# # save token to id mapping as a txt file
# with open(os.path.join(vocab_dir, '{}_mapping.txt'.format(vocab_name)), mode='w', encoding='utf-8') as f:
#     for token, index in sorted(tokenizer.get_vocab().items(), key=lambda item: item[1]):
#         f.write('{}\t{}\n'.format(token, index))
#
# from data.vocab import Vocab
# from tokenizers import Tokenizer
# from data.vocab import Vocab
#
# tokenizer = Tokenizer.from_file('test_outputs/test/test_tokenizer.json')
#
# codes = ['public TcpMatcher ( final NetworkConfig config ) { super ( config ) ; }',
#          'public TcpMatcher ( final NetworkConfig config )']
#
# tokenizer.post_processor = Vocab.bert_processor
# encoded = tokenizer.encode_batch(codes)
# print(encoded[0].ids)
# print(encoded[1].ids)
# print(encoded[0].attention_mask)
# print(encoded[1].attention_mask)

# print('-' * 100)
#
# tokenizer.post_processor = Vocab.eos_processor
# tokenizer.enable_truncation(10)
# encoded = tokenizer.encode_batch(codes)
# print(encoded[0].ids)
# print(encoded[1].ids)
# print(encoded[0].attention_mask)
# print(encoded[1].attention_mask)
#
#
# def generate_subsequent_mask(length, batch_size):
#     import numpy as np
#     import torch
#     mask = np.tril(np.ones([length, length]))  # Upper triangular matrix
#     mask = torch.from_numpy(mask).long()
#     mask = mask.unsqueeze(0).repeat(batch_size, 1, 1)
#     return mask
#
#
# subsequent_mask = generate_subsequent_mask(10, 2)
# print(subsequent_mask)

# import argparse
# from main import add_args
# from data.dataset import load_dataset
# from datasets import Dataset
#
# parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.register('type', 'bool', lambda v: v.lower() in ['yes', 'true', 't', '1', 'y'])
# add_args(parser)
# main_args = parser.parse_args()
#
# dataset, _ = load_dataset(args=main_args, mode='valid')
#
# for index, example in enumerate(dataset):
#     print(example)
#     break


# import json
# import re
#
# from data.code_tokenizer.tokenizer import TokeNizer
#
# # map the language names between internal and ``code_tokenizer``
# CODE_TOKENIZER_MAPPING = {'python': TokeNizer('Python'),
#                           'java': TokeNizer('Java'),
#                           'javascript': TokeNizer('JavaScript'),
#                           'ruby': TokeNizer('Ruby'),
#                           'go': TokeNizer('Go'),
#                           'php': TokeNizer('PHP')}
#
#
# def get_source(lang):
#     sources = []
#     with open(f'../../dataset/pre_train/{lang}/valid/{lang}_valid_0.jsonl') as f:
#         for line in f.readlines():
#             data = json.loads(line.strip())
#             source = data['code']
#             sources.append(source)
#     return sources
#
#
# def trim_spaces(source):
#     return re.sub(r'\s+', ' ', source)
#
#
# sources = get_source('java')
# for source in sources:
#     tokens = CODE_TOKENIZER_MAPPING['java'].getPureTokens(source)
#     print(trim_spaces(' '.join(tokens)))


# import json
# import random
# import re
# from data.data_utils import *
#
#
# lang = 'go'
#
#

# import json
# import random
# import re
#
#
# def lang_sample(lang):
#     with open(f'../../dataset/pre_train/{lang}/valid/{lang}_valid_0.jsonl') as f:
#         line = f.readlines()[random.randint(0, 1000)]
#         data = json.loads(line.strip())
#         name = data['func_name']
#         source = data['code']
#         code = ' '.join(data['code_tokens'])
#     return source, code, name
# #
# #
# # def sample_separation_position(source):
# #     matches = re.finditer(r"\b\S", source)
# #     indices = [m.start(0) for m in matches]
# #     return random.sample(indices, 1)[0]
# #
# #
# # source, _, _ = lang_sample(lang)
# #
# # idx = sample_separation_position(source)
# #
# # print(source)
# # print('-' * 100)
# # print(source[:idx])
# # print('-' * 100)
# # print(source[idx:])
#
#
# source, _, _ = lang_sample(lang)
#
# code = tokenize_source(source, lang)
#
# print(source)
# print('-' * 100)
# print(code)

#
# from data.data_utils import count_non_space_chars
#
# s = ' \n\r\t'
# print(count_non_space_chars(s))


# import tokenize
# from io import StringIO
# from data.data_utils import remove_comments_and_docstrings, replace_string_literal, trim_spaces
# import nltk
# #
# #
# lang = 'php'
# source, _, _ = lang_sample(lang)
# source = remove_comments_and_docstrings(source, lang)
# source = replace_string_literal(source)
#
#
# def regular_tokenize(source: str):
#     source = re.sub(r'(\S)[.=](\S)', r'\1 . \2', source)
#     return nltk.word_tokenize(source)
#
#
# # def tokenize_python(source):
# #     tokens = tokenize.generate_tokens(StringIO(source).readline)
# #     return ' '.join([token.string for token in tokens])
# #
# print(source)
# print('-' * 100)
# print('\n'.join(regular_tokenize(source)))


# import numpy as np
#
#
# vectors = []
# for i in range(10):
#     rep = np.random.rand(16, 256)
#     vectors.append(rep)
# vectors.append(np.random.rand(10, 256))
#
# vectors = np.concatenate(vectors, 0)
# print(vectors.shape)


# batch = [('a1', 'b1'),
#          ('a2', 'b2'),
#          ('a3', 'b3')]

# a, b = map(list, zip(*batch))

# print(a)
# print(b)
#
# model_inputs = {'input_ids': a, 'attention_mask': b}
# model_inputs['urls'] = ['dfadf', 'dfadf']
#
# print(model_inputs)
# urls = model_inputs.pop('urls')
# print(urls)
# print(model_inputs)
