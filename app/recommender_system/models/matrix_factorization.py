import torch
import torch.nn as nn
import torch.nn.functional as F

# from utils import *

def l2_regularization(x):
    return torch.sum(x ** 2.)

class MatrixFactorization(nn.Module):
    def __init__(self, num_users, num_items, l2_alpha, latent_dim=64):
        super(MatrixFactorization, self).__init__()
        self.l2_alpha = l2_alpha

        self.users = nn.Embedding(num_users, latent_dim, sparse=True)
        self.items = nn.Embedding(num_items, latent_dim, sparse=True)

    def __call__(self, x):
        users = self.users(x[:, 0])
        items = self.items(x[:, 1])

        users = torch.unsqueeze(users, dim=1)
        items = torch.unsqueeze(items, dim=-1)

        predictions = torch.bmm(users, items)

        predictions = predictions.squeeze()

        return predictions

    def loss(self, predictions, ground_truths):
        loss = F.mse_loss(predictions, ground_truths)

        user_prior = l2_regularization(self.users.weight)
        item_prior = l2_regularization(self.items.weight)

        loss += self.l2_alpha * (user_prior + item_prior)

        return loss
