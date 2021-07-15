
from collections import Counter
import re

from .bleu.google_bleu import avg_bleu
from .meteor.meteor import Meteor
from .rouge.rouge import Rouge


def ir_metrics(references, candidates):
    """
    An ir metrics for a list of references and candidates, each of both is a single token so that need exact match.

    Args:
        references (list[str]): A list of references, each reference should be one token
        candidates (list[str]): A list of candidates, each candidate should be one token

    Returns:
        (float, float, float):
            - precision
            - recall
            - f1
    """
    p, r, f1 = 0, 0, 0
    if len(references) == 0:
        if len(candidates) == 0:
            p, r, f1 = 1, 1, 1
    else:
        common = Counter(candidates) & Counter(references)
        num_same = sum(common.values())
        if num_same != 0:
            p = 1.0 * num_same / len(candidates)
            r = 1.0 * num_same / len(references)
            f1 = (2 * p * r) / (p + r)
    return p, r, f1


def avg_ir_metrics(references, candidates):
    """
    Calculate precision, recall and f1 score,
    this version of ir metrics calculate the avg scores of each candidate in candidates.

    Args:
        references (list[list[str]]): A list of references, each reference should be tokenized into a list of tokens
        candidates (list[list[str]]): A list of candidates, each candidate should be tokenized into a list of tokens

    Returns:
        dict: Dict of mapping ir metric names to scores
    """
    total_p, total_r, total_f1 = 0, 0, 0
    for reference, candidate in zip(references, candidates):
        p, r, f1 = ir_metrics(references=reference, candidates=candidate)

        total_p += p
        total_r += r
        total_f1 += f1

    size = len(references)
    return {'avg_precision': total_p / size, 'avg_recall': total_r / size, 'avg_f1': total_f1 / size}


def remove_white_characters(tokens):
    """
    Join the list of tokens and remove all white characters.

    Args:
        tokens (list[str]): List of tokens

    Returns:
        str: String after removing white characters

    """
    s = ''.join(tokens).lower()
    return re.sub(r'\s', '', s)


def exact_ir_metrics(references, candidates):
    """
    Calculate precision, recall and f1 score,
        this version of ir metrics calculate scores of each candidate in candidates
        which match the corresponding reference exactly (except white characters).

    Args:
        references (list[list[str]]): A list of references, each reference should be tokenized into a list of tokens
        candidates (list[list[str]]): A list of candidates, each candidate should be tokenized into a list of tokens

    Returns:
        dict: Dict of mapping ir metric names to scores
    """
    text_references = [remove_white_characters(ref) for ref in references]
    text_candidates = [remove_white_characters(can) for can in candidates]
    p, r, f1 = ir_metrics(references=text_references, candidates=text_candidates)
    return {'exact_precision': p, 'exact_recall': r, 'exact_f1': f1}


def bleu(references, candidates):
    return {'bleu': avg_bleu(references=references, candidates=candidates)}


def meteor(references, candidates):
    meteor_calculator = Meteor()
    return {'meteor': meteor_calculator.compute_score(references=references, candidates=candidates)[0]}


def rouge_l(references, candidates):
    rouge_calculator = Rouge()
    return {'rouge-l': rouge_calculator.compute_score(references=references, candidates=candidates)[0]}
