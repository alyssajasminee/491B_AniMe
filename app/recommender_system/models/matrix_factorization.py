import torch
import torch.nn as nn

class MatrixFactorization(nn.Module):
    def __init__(self, factor_dim=64):
