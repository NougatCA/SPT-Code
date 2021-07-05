
import torch

from prettytable import PrettyTable


def to_time(float_time):
    """
    translate float time to h, min, s and ms
    :param float_time: time in float
    :return: h, min, s, ms
    """
    time_s = int(float_time)
    time_ms = int((float_time - time_s) * 1000)
    time_h = time_s // 3600
    time_s = time_s % 3600
    time_min = time_s // 60
    time_s = time_s % 60
    return time_h, time_min, time_s, time_ms


def time2str(float_time):
    time_h, time_min, time_s, time_ms = to_time(float_time)
    return '{}h {}min {}s {}ms'.format(time_h, time_min, time_s, time_ms)


def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'),
                         ['', 'K', 'M', 'B', 'T'][magnitude])


def count_params(model):
    """
    Count the number of parameters of given model
    """
    return sum(p.numel() for p in model.parameters())


def layer_wise_parameters(model):
    table = PrettyTable()
    table.field_names = ["Layer Name", "Output Shape", "Param #"]
    table.align["Layer Name"] = "l"
    table.align["Output Shape"] = "r"
    table.align["Param #"] = "r"
    for name, parameters in model.named_parameters():
        if parameters.requires_grad:
            table.add_row([name, str(list(parameters.shape)), parameters.numel()])
    return table


def init_module_params(module: torch.nn.Module):
    """
    Initialize the parameters of the given module
    """
    if isinstance(module, torch.nn.RNNBase):
        for name, param in module.named_parameters():
            if 'weight' in name:
                torch.nn.init.xavier_normal_(param)
            elif 'bias' in name:
                torch.nn.init.normal_(param)
    elif isinstance(module, torch.nn.Linear):
        torch.nn.init.xavier_normal_(module.weight.data)
        if module.bias is not None:
            torch.nn.init.normal_(module.bias.data)
    elif isinstance(module, torch.nn.Embedding):
        torch.nn.init.uniform_(module.weight, -0.1, 0.1)
