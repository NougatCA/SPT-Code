
import torch
from typing import Dict


def inputs_to_cuda(inputs: Dict[str, torch.Tensor]):
    """
    Move tensors in the inputs to cuda.

    Args:
        inputs (dict[str, torch.Tensor]): Inputs dict

    Returns:
        dict[str, torch.Tensor]: Moved inputs dict

    """
    if not torch.cuda.is_available():
        return inputs
    for key, value in inputs.items():
        if isinstance(value, torch.Tensor):
            inputs[key] = value.cuda()
    return inputs
