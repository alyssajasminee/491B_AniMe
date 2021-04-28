import os
import h5py
import torch
import numpy as np

from tqdm import tqdm
from torch.autograd import Variable
from recommender_system.models.matrix_factorization import MatrixFactorization


def load_data(infile, split='train', verbose=False):
    '''
        This function loads the image data from a HDF5 file
        Args:
          outfile: string, path to read file from

        Returns:
          f["image"][()]: numpy.array, image data as numpy array
    '''
    path = os.path.join(infile, split + '.hdf5')

    if verbose:
        print("---------------------------------------")
        print("Loading data")
        print("---------------------------------------\n")
    with h5py.File(path, "r") as f:
        features = f["features"][()]
        gts = f["gts"][()]

    return features, gts


def get_model(config, train=True, load_path=None, device=None):
    model_type = config['MODEL']
    num_users  = config['NUM_USERS']
    num_items  = config['NUM_ITEMS']
    latent_dim = config['LATENT_DIM']

    lr = config['LR']
    l2_alpha = config['L2_ALPHA']

    if model_type == 'mat_factor':
        model = MatrixFactorization(num_users,
                                    num_items,
                                    l2_alpha,
                                    latent_dim=latent_dim)
    elif model_type == 'bayes_mf':
        pass
    elif model_type == 'boltzmann':
        pass

    if load_path is not None:
        if device is not None:
            state_dict = torch.load(load_path, map_location=device)
        else:
            state_dict = torch.load(load_path)
        model.load_state_dict(state_dict)

    else:
        model.cuda()

    if train:
        optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=.99, nesterov=True)
        sched = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.75)

        return {'model_type': model_type,
                'model': model,
                'optimizer': optimizer,
                'sched': sched
                }

    else:
        model.eval()
        return model


def train(model_dict, data_loader, epochs, predict=False):
    model_type = model_dict['model_type']
    model = model_dict['model']
    optimizer = model_dict['optimizer']
    sched = model_dict['sched']

    for epoch in range(epochs):
        losses = []
        for data in tqdm(data_loader):
            user_items, ratings = data

            if predict:
                ratings = ratings.float()

            else:
                user_items = Variable(user_items.cuda())
                ratings = Variable(ratings.cuda()).float()

            optimizer.zero_grad()

            recommendations = model(user_items)

            loss = model.loss(recommendations, ratings)
            loss.backward()

            optimizer.step()

            losses.append(loss.item())

        print('Epoch {}/{} ...... Training loss: {}'.format(epoch+1, epochs, np.mean(losses)))
        torch.save(model.state_dict(), os.path.join('./models', model_type + '.pth'))


def eval(model, data_loader):
    losses = []
    with torch.no_grad():
        for data in tqdm(data_loader):
            user_items, ratings = data

            ratings = ratings.float()

            recommendations = model(user_items)

            loss = model.loss(recommendations, ratings)
            losses.append(loss.item())

    print('Test loss: {}'.format(np.mean(losses)))
