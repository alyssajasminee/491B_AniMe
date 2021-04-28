#!/usr/bin/python
import yaml

from utils import *
from data.UserAnimeDataset import UserAnimeDataset

with open('./configs/config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

if __name__ == "__main__":
    batch_size = config['BATCH_SIZE']
    num_epochs = config['NUM_EPOCHS']

    X_train, Y_train = load_data('./data', verbose=True)
    train_dataset = UserAnimeDataset(X_train, labels=Y_train, predict=False)
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                               batch_size=batch_size,
                                               shuffle=True)

    model_dict = get_model(config)

    train(model_dict, train_loader, num_epochs)
