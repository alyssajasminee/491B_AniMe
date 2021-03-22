import torch
import torch.nn as nn
import torch.nn.functional as F

from utils import l2_regularization


class MatrixFactorization(nn.Module):
    def __init__(self, num_users, num_items, l2_alpha, factor_dim=64):
        super(MatrixFactorization, self).__init__()
        self.l2_alpha = l2_alpha

        self.users = nn.Embedding(num_users, factor_dim)
        self.items = nn.Embedding(num_items, factor_dim)

    def __call__(self, x):
        users = self.users(x[:, 0])
        items = self.items(x[:, 1])

        predictions = torch.sum(users * items, dim=1)

        return predictions

    def loss(self, predictions, ground_truths):
        loss = F.mse_loss(predictions, ground_truths)

        user_prior = l2_regularization(self.users.weight)
        item_prior = l2_regularization(self.items.weight)

        loss += self.l2_alpha * (user_prior + item_prior)

        return loss
