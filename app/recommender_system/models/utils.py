import torch

def l2_regularization(x):
    return torch.sum(x ** 2.)