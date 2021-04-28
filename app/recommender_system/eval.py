#!/usr/bin/python
import yaml

from utils import *
from data.UserAnimeDataset import UserAnimeDataset

with open('./configs/config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

if __name__ == "__main__":
    model_type = config['MODEL']
    batch_size = config['BATCH_SIZE']
    num_epochs = config['NUM_EPOCHS']

    X_test, Y_test = load_data('./data', verbose=True)
    test_dataset = UserAnimeDataset(X_test, labels=Y_test, predict=False)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                              batch_size=1,
                                              shuffle=False)

    model_path = os.path.join('./models', model_type + '.pth')

    model = get_model(config, train=False, load_path=model_path)

    eval(model, test_loader)
