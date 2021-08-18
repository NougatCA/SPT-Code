
from collections import Counter
import re
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

from .bleu.google_bleu import avg_bleu
from .meteor.meteor import Meteor
from .rouge.rouge import Rouge


def ir_metrics(references, candidates):
    """
    An ir metrics for binary classification.

    Args:
        references (list[int]): A list of references, each reference should be 0 or 1
        candidates (list[int]): A list of candidates, each candidate should be 0 or 1

    Returns:
        dict[str, int]: Mapping metric names to scores

    """
    p = precision_score(y_true=references, y_pred=candidates)
    r = recall_score(y_true=references, y_pred=candidates)
    f1 = f1_score(y_true=references, y_pred=candidates)
    return {'precision': p, 'recall': r, 'f1': f1}


def __ir_metrics(references, candidates):
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
        p, r, f1 = __ir_metrics(references=reference, candidates=candidate)

        total_p += p
        total_r += r
        total_f1 += f1

    size = len(references)
    return {'avg_precision': total_p / size, 'avg_recall': total_r / size, 'avg_f1': total_f1 / size}


def remove_white_characters(s):
    """
    Join the list of tokens and remove all white characters.

    Args:
        s (Union(list[str], str)): List of tokens

    Returns:
        str: String after removing white characters

    """
    if isinstance(s, list):
        s = ''.join(s)
    s = s.lower()
    s = re.sub(r'\s', '', s)
    return s


def accuracy_for_sequence(references, candidates):
    """
    Calculate accuracy,
        this version of ir metrics calculate scores of each candidate in candidates
        which match the corresponding reference exactly (except white characters).

    Args:
        references (list[list[str]]): A list of references, each reference should be a list of tokens
        candidates (list[list[str]]): A list of candidates, each candidate should be a list of tokens

    Returns:
        dict[str, float]: Dict of mapping ir metric names to scores

    """
    references = [remove_white_characters(reference) for reference in references]
    candidates = [remove_white_characters(candidate) for candidate in candidates]
    return accuracy(references=references, candidates=candidates)


def accuracy(references, candidates):
    """
    Calculate accuracy.

    Args:
        references (list): A list of references, each reference should be an object
        candidates (list): A list of candidates, each candidate should be an object

    Returns:
        dict[str, float]: Dict of mapping ir metric names to scores

    """
    acc = accuracy_score(y_true=references, y_pred=candidates)
    return {'accuracy': acc}


def accuracy_top_k_for_sequence(references, candidates):
    """
    Calculate accuracy,
        this version of ir metrics calculate scores of each candidate in candidates
        which match the corresponding reference exactly (except white characters).

    Args:
        references (list[str]): A list of references, each reference should be a string
        candidates (list[list[str]]): A list of candidates, each candidate should be a list of string

    Returns:
        dict[str, float]: Dict of mapping ir metric names to scores

    """
    references = [remove_white_characters(reference) for reference in references]
    candidates = [[remove_white_characters(can) for can in candidate] for candidate in candidates]
    return accuracy_top_k(references=references, candidates=candidates)


def accuracy_top_k(references, candidates):
    """
    Calculate accuracy for top k.

    Args:
        references (list): A list of references, each reference should be an object
        candidates (list[list]): A list of candidates, each candidate should be a list of k candidates

    Returns:
        dict[str, float]: Dict of mapping ir metric names to scores

    """
    k = len(candidates[0])
    acc_top_k = {}
    for i in range(1, k + 1):
        acc_top_k[f'accuracy_top_{i}'] = 0
    for reference, candidate_list in zip(references, candidates):
        for i in range(1, k + 1):
            candidate_set = set(candidate_list[:i])
            if reference in candidate_set:
                acc_top_k[f'accuracy_top_{i}'] += 1
    for key, value in acc_top_k.items():
        acc_top_k[key] = value / len(references)
    return acc_top_k


def bleu(references, candidates):
    """
    Calculate avg BLEU.

    Args:
        references (list[list[str]]): A list of references, each reference should be tokenized into a list of tokens
        candidates (list[list[str]]): A list of candidates, each candidate should be tokenized into a list of tokens

    Returns:
        dict[str, float]: Dict of mapping metric name and avg score

    """
    return {'bleu': avg_bleu(references=references, candidates=candidates)}


def meteor(references, candidates):
    """
    Calculate avg METEOR.

    Args:
        references (list[list[str]]): A list of references, each reference should be tokenized into a list of tokens
        candidates (list[list[str]]): A list of candidates, each candidate should be tokenized into a list of tokens

    Returns:
        dict[str, float]: Dict of mapping metric name and avg score

    """
    meteor_calculator = Meteor()
    return {'meteor': meteor_calculator.compute_score(references=references, candidates=candidates)[0]}


def rouge_l(references, candidates):
    """
    Calculate avg ROUGE-L.

    Args:
        references (list[list[str]]): A list of references, each reference should be tokenized into a list of tokens
        candidates (list[list[str]]): A list of candidates, each candidate should be tokenized into a list of tokens

    Returns:
        dict[str, float]: Dict of mapping metric name and avg score

    """
    rouge_calculator = Rouge()
    return {'rouge-l': rouge_calculator.compute_score(references=references, candidates=candidates)[0]}
