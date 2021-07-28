from tokenizers import Tokenizer
from tokenizers.models import BPE, WordLevel
from tokenizers.trainers import BpeTrainer, WordLevelTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers import normalizers
from tokenizers.normalizers import Strip, Lowercase, NFD, StripAccents
from tokenizers.processors import TemplateProcessing, BertProcessing

import pickle
import os
import logging

from typing import List, Union

logger = logging.getLogger(__name__)


class Vocab(object):
    # special vocabulary symbols
    PAD_TOKEN = '[PAD]'  # padding token
    SOS_TOKEN = '[SOS]'  # start of sequence, also CLS
    EOS_TOKEN = '[EOS]'  # end of sequence
    UNK_TOKEN = '[UNK]'  # unknown token
    MSK_TOKEN = '[MSK]'  # mask token
    SEP_TOKEN = '[SEP]'  # sentence separator token
    # CLS_TOKEN = '[CLS]'     # classification placeholder

    # default special symbols, if need additional symbols, use init parameter 'additional_special_symbols'
    START_VOCAB = [PAD_TOKEN, SOS_TOKEN, EOS_TOKEN, UNK_TOKEN, MSK_TOKEN, SEP_TOKEN]

    # post-processors
    # bert processor: add SOS at the beginning and SEP at the end of sequence
    # bert_processor = BertProcessing(sep=(SEP_TOKEN, START_VOCAB.index(EOS_TOKEN)),
    #                                 cls=(SOS_TOKEN, START_VOCAB.index(SOS_TOKEN)))
    # sos processor: add SOS at the beginning of sequence
    sos_processor = TemplateProcessing(single=f'{SOS_TOKEN} $', pair=f'{SOS_TOKEN} $A $B',
                                       special_tokens=[(SOS_TOKEN, START_VOCAB.index(SOS_TOKEN))])
    # eos processor: add EOS at the end of sequence
    eos_processor = TemplateProcessing(single=f'$ {EOS_TOKEN}', pair=f'$A $B {EOS_TOKEN}',
                                       special_tokens=[(EOS_TOKEN, START_VOCAB.index(EOS_TOKEN))])
    # sep processor: add SEP at the end of sequence
    sep_processor = TemplateProcessing(single=f'$ {SEP_TOKEN}', pair=f'$A $B {SEP_TOKEN}',
                                       special_tokens=[(SEP_TOKEN, START_VOCAB.index(SEP_TOKEN))])

    def __init__(
            self,
            name,
            method,
            vocab_size=None,
            datasets: Union[List[str], List[List[str]]] = None,
            additional_special_symbols=None,
            ignore_case=False,
            save_root=None,
            index_offset=None,
    ):
        """
        Initialize a vocabulary and train the tokenizer.

        Args:
            name (str): Vocabulary name
            method (str): Tokenize method
            vocab_size (int): Maximum size of the vocabulary
            datasets (Union[List[str], List[List[str]]]): List of (file paths/list of string) to train the tokenizer
            additional_special_symbols (list[str]): Optional, list of custom special symbols
            ignore_case (bool): Ignore cases if True, default False
            save_root (str): Optional, if given, save to given root
            index_offset (int): Optional, the index offset when encoding and decoding.

        """
        assert method in ['word', 'bpe'], \
            'Tokenize method not supported, given {}, expect \'word\' or \'bpe\''.format(method)

        self.name = name
        self.method = method
        self.__special_symbols = Vocab.START_VOCAB.copy()
        if additional_special_symbols:
            self.add_special_symbols(additional_special_symbols)
        self.ignore_case = ignore_case

        if index_offset is not None and index_offset != 0:
            self.index_offset = index_offset
        else:
            self.index_offset = None

        # tokenizer and trainer
        if method == 'word':
            tokenize_class = WordLevel
            trainer_class = WordLevelTrainer
        else:
            if vocab_size is None:
                logger.warning('It is recommended to specific the vocabulary size for BPE tokenize method')
            tokenize_class = BPE
            trainer_class = BpeTrainer

        self.tokenizer = Tokenizer(tokenize_class(unk_token=Vocab.UNK_TOKEN))
        if vocab_size:
            trainer = trainer_class(special_tokens=self.__special_symbols, vocab_size=vocab_size)
        else:
            trainer = trainer_class(special_tokens=self.__special_symbols)
        self.tokenizer.pre_tokenizer = Whitespace()

        # normalizer
        if ignore_case:
            normalizer = normalizers.Sequence([NFD(), StripAccents(), Strip(), Lowercase()])
        else:
            normalizer = normalizers.Sequence([NFD(), StripAccents(), Strip()])
        self.tokenizer.normalizer = normalizer

        # train tokenizer
        if isinstance(datasets[0], str):
            self.tokenizer.train(files=datasets, trainer=trainer)
        elif isinstance(datasets[0], list):
            self.tokenizer.train_from_iterator(iterator=datasets, trainer=trainer)
        else:
            raise TypeError('The type of datasets is not support, expect list of paths or list of lines')

        # pad idx
        self.pad_token_id = self.get_pad_index()

        # save
        if save_root:
            self.save(vocab_root=save_root)

    def add_special_symbols(self, symbols: list):
        assert isinstance(symbols, list)
        for symbol in symbols:
            assert isinstance(symbol, str)
            if symbol not in self.__special_symbols:
                self.__special_symbols.append(symbol)

    def get_index(self, token: str) -> int:
        """
        Return the index of given word, if the given word is not in the vocabulary, return the index of UNK token.

        Args:
            token (str): Word in str

        Returns:
            int: Index of the given word, [UNK] if OOV

        """
        if self.ignore_case:
            token = token.lower()
        index = self.tokenizer.token_to_id(token)
        if self.index_offset and token not in self.__special_symbols:
            index += self.index_offset
        return index if index else self.tokenizer.token_to_id(Vocab.UNK_TOKEN)

    def get_token(self, index: int) -> str:
        """
        Return the corresponding token of the given index, if not in the vocabulary, return index of UNK.

        Args:
            index: Given index

        Returns:
            str: Token of the given index

        """
        if self.index_offset:
            if index >= (len(self.__special_symbols) + self.index_offset):
                index -= self.index_offset
            elif len(self.__special_symbols) <= index < (len(self.__special_symbols) + self.index_offset):
                index = self.get_unk_index()
        token = self.tokenizer.id_to_token(index)
        return token if token else Vocab.UNK_TOKEN

    def transfer_index(self, index):
        """
        Return the transferred index based on the index offset

        Args:
            index (int): Index to transfer

        Returns:
            int: Transferred index

        """
        if not self.index_offset or index < len(self.__special_symbols):
            return index
        return index + self.index_offset

    def restore_index(self, index):
        """
        Return the restored index based on the base index

        Args:
            index (int): Index to restore

        Returns:
            int: Restored index

        """
        if not self.index_offset or index < len(self.__special_symbols):
            return index
        if index < self.index_offset:
            return self.get_unk_index()
        return index - self.index_offset

    def encode_sequence(self, sequence: Union[str, List[str]], is_pre_tokenized=False):
        """
        Encode a sequence to corresponding ids.

        Args:
            sequence (Union[str, List[str]]): Sequence to be encoded,
                when is_pre_tokenized is False, the type should be str,
                when is_pre_tokenized is True, the type should be List[str]
            is_pre_tokenized (bool): Whether the input is already pre-tokenized

        Returns:
            list[int], list[int]: indices and mask for sequence

        """
        if self.ignore_case:
            sequence = sequence.lower()
        encoded = self.tokenizer.encode(sequence=sequence, is_pretokenized=is_pre_tokenized)
        ids = [self.transfer_index(index) for index in encoded.ids]
        return ids, encoded.attention_mask

    def encode_batch(self, batch: Union[List[str], List[List[str]]], is_pre_tokenized=False,
                     pad=False, max_length=None):
        """
        Encode a batch of sequences.

        Args:
            batch (Union[List[str], List[List[str]]]): batch of sequences to be encoded,
                when is_pre_tokenized is False, the type should be List[str],
                when is_pre_tokenized is True, the type should be List[List[str]]
            is_pre_tokenized (bool): Whether the input is already pre-tokenized
            pad (bool): Whether to pad each of the sequence
            max_length (int): The length to padding

        Returns:
            (list[list[int]], list[list[int]]):
                - encoded batch of indices
                - encoded batch of attention masks

        """
        if self.ignore_case:
            batch = [sequence.lower() if isinstance(sequence, str) else [token.lower() for token in sequence]
                     for sequence in batch]
        if pad:
            self.tokenizer.enable_padding(length=max_length)
        else:
            self.tokenizer.no_padding()
        encoded_batch = self.tokenizer.encode_batch(input=batch, is_pretokenized=is_pre_tokenized)
        ids = [[self.transfer_index(index) for index in encoded.ids] for encoded in encoded_batch]
        attention_mask = [encoded.attention_mask for encoded in encoded_batch]
        return ids, attention_mask

    def decode(self, ids: List[int], skip_special_tokens=True) -> str:
        """
        Decode the given list of ids back to a string.

        Args:
            ids (list[int]): The list of ids that we want to decode
            skip_special_tokens (bool): Whether the special tokens should be removed from the decoded string,
                default True

        Returns:
            str: The decoded string

        """
        if self.index_offset:
            ids = [self.restore_index(index) for index in ids]
        return self.tokenizer.decode(ids=ids, skip_special_tokens=skip_special_tokens)

    def decode_batch(self, batch: List[List[int]], skip_special_tokens=True) -> List[str]:
        """
        Decode a batch of ids back to their corresponding string.

        Args:
            batch (list[list[str]]): The batch of sequences we want to decode
            skip_special_tokens (bool): Whether the special tokens should be removed from the decoded string,
                default True

        Returns:
            list[str]: The list of decoded string

        """
        if self.index_offset:
            batch = [[self.restore_index(index) for index in seq] for seq in batch]
        return self.tokenizer.decode_batch(sequences=batch, skip_special_tokens=skip_special_tokens)

    def get_pad_index(self):
        return self.tokenizer.token_to_id(Vocab.PAD_TOKEN)

    def get_sos_index(self):
        return self.tokenizer.token_to_id(Vocab.SOS_TOKEN)

    def get_eos_index(self):
        return self.tokenizer.token_to_id(Vocab.EOS_TOKEN)

    def get_unk_index(self):
        return self.tokenizer.token_to_id(Vocab.UNK_TOKEN)

    def get_mask_index(self):
        return self.tokenizer.token_to_id(Vocab.MSK_TOKEN)

    def save(self, vocab_root, name=None):
        """
        Save the vocabulary to the given directory.

        Args:
            vocab_root (str): Parent directory to be saved
            name (str): Vocabulary name

        """
        vocab_name = name if name else self.name
        vocab_dir = os.path.join(vocab_root, vocab_name)
        if not os.path.exists(vocab_dir) or not os.path.isdir(vocab_dir):
            os.makedirs(vocab_dir)

        # save pickle file for whole instance
        with open(os.path.join(vocab_dir, '{}.pk'.format(vocab_name)), mode='wb') as f:
            pickle.dump(self, f)
        # save tokenizer
        self.tokenizer.save(os.path.join(vocab_dir, '{}_tokenizer.json'.format(vocab_name)))
        # save token to id mapping as a txt file
        with open(os.path.join(vocab_dir, '{}_mapping.txt'.format(vocab_name)), mode='w', encoding='utf-8') as f:
            for token, index in sorted(self.tokenizer.get_vocab().items(), key=lambda item: item[1]):
                f.write('{}\t{}\n'.format(token, index))

    def save_pretrained(self, output_dir):
        return

    def num_special_token(self):
        return len(self.__special_symbols)

    def save_pickle(self, path):
        """Save to binary pickle file"""
        with open(path, mode='wb') as f:
            pickle.dump(self, f)
        logger.info(f'Vocab saved to {path}')

    def __len__(self):
        return self.tokenizer.get_vocab_size()

    def __contains__(self, item):
        """
        Return True if the given token is in the vocab, else False.

        Args:
            item (str): Word to query

        Returns:
            bool: True if the given token is in the vocab, else False.

        """
        if self.ignore_case:
            item = item.lower()
        return True if self.tokenizer.token_to_id(item) else False


def load_vocab(vocab_root, name) -> Vocab:
    """
    Load vocabulary instance from pickle file, which should locates in the sub-directory named given vocabulary name.

    Args:
        vocab_root (BytesPath): Root of the vocabulary
        name (str): Name of the vocabulary

    Returns:
        Vocab: Loaded vocab instance

    """
    with open(os.path.join(vocab_root, name, '{}.pk'.format(name)), mode='rb') as f:
        obj = pickle.load(f)
    assert isinstance(obj, Vocab)
    return obj


def init_vocab(vocab_save_dir,
               name,
               method='word',
               vocab_size=None,
               datasets: Union[List[str], List[List[str]]] = None,
               additional_special_symbols=None,
               ignore_case=False,
               save_root=None,
               index_offset=None,
               load_if_saved=True) -> Vocab:
    vocab_name = '.'.join(
        [sub_name for sub_name in [name, method, str(vocab_size), str(index_offset)] if sub_name is not None])
    path = os.path.join(vocab_save_dir, f'{vocab_name}.pk')
    if load_if_saved:
        if os.path.exists(path) and os.path.isfile(path):
            logger.info(f'Trying to load saved binary pickle file from: {path}')
            with open(path, mode='rb') as f:
                obj = pickle.load(f)
            assert isinstance(obj, Vocab)
            if save_root:
                obj.save(save_root)
            return obj
    vocab = Vocab(name=name,
                  method=method,
                  vocab_size=vocab_size,
                  datasets=datasets,
                  additional_special_symbols=additional_special_symbols,
                  ignore_case=ignore_case,
                  save_root=save_root,
                  index_offset=index_offset)
    vocab.save_pickle(path)
    return vocab
