from torch.utils.data import Dataset

class UserAnimeDataset(Dataset):
    def __init__(self, data, labels=None, predict=False):
        self.data = data
        self.predict = predict
        if not self.predict:
            self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        label = None
        if not self.predict:
            sample_label = self.labels[idx]
            return sample, sample_label
        return sample
