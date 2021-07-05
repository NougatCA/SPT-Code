
from collections import Counter

from .bleu.google_bleu import avg_bleu
from .meteor.meteor import Meteor
from .rouge.rouge import Rouge


def ir_metrics(references, candidates):
    """
    An ir metrics for a list of references and candidates, each of both is a single token so that need exact match.

    Args:
        references: A list of references, each reference should be one token
        candidates: A list of candidates, each candidate should be one token

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
        references (list): A list of references, each reference should be tokenized into a list of tokens
        candidates (list): A list of candidates, each candidate should be tokenized into a list of tokens

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
    return {'precision': total_p / size, 'recall': total_r / size, 'f1': total_f1 / size}


def bleu(references, candidates):
    return {'bleu': avg_bleu(references=references, candidates=candidates)}


def meteor(references, candidates):
    meteor_calculator = Meteor()
    return {'meteor': meteor_calculator.compute_score(references=references, candidates=candidates)[0]}


def rouge_l(references, candidates):
    rouge_calculator = Rouge()
    return {'rouge-l': rouge_calculator.compute_score(references=references, candidates=candidates)[0]}
