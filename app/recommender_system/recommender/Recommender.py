import yaml
import backend.DBController as dbc

import os
import torch

from sklearn.neighbors import BallTree
from recommender_system.utils import get_model


class Recommender:
    def __init__(self):
        with open('../491B_AniMe/app/recommender_system/configs/config.yaml', 'r') as stream:
            self.settings = yaml.safe_load(stream)

        self.model_type = self.settings['MODEL']

        model_path = os.path.join('../491B_AniMe/app/recommender_system/models', self.model_type + '.pth')
        self.model_dict = get_model(self.settings, load_path=model_path, device=torch.device('cpu'))

    def get_item_idxs(self, user_id):
        rdb_controller = dbc.DBController().reviewDB
        reviews_db = rdb_controller.get_reviews()

        pipeline = [
            {
                '$group': {'_id': '_id', 'max_id': {'$max': '$new_anime_id'}}
            }
        ]

        max_item_id = reviews_db.aggregate(pipeline)
        max_item_id = list(max_item_id)
        max_item_id = max_item_id[0]['max_id']

        all_idxs = set(range(max_item_id))

        query = {'new_user_id': user_id}
        user_ratings = reviews_db.find(query)
        user_ratings = list(user_ratings)

        rated_items = [rating_dict['new_anime_id'] for rating_dict in user_ratings]

        rated_idxs = set(rated_items)
        item_idxs = list(all_idxs - rated_idxs)

        return item_idxs

    def recommend(self, user_id, k=10):
        uidx_controller = dbc.DBController().userIdxDB
        aidx_controller = dbc.DBController().animeIdxDB

        user_id = uidx_controller.get_new_user_id(user_id)

        item_idxs = self.get_item_idxs(user_id)

        items = self.model_dict['model'].items(torch.LongTensor(item_idxs)).detach().numpy()
        ball_tree = BallTree(items, leaf_size=33)

        query = self.model_dict['model'].users(torch.LongTensor([user_id])).detach().numpy()

        _, idxs = ball_tree.query(query, k=k)

        recommended_items = []
        for idx in idxs[0]:
            recommended_item = items[idx]
            item_embeddings = self.model_dict['model'].items.weight.data

            distance = torch.norm(item_embeddings - recommended_item, dim=1)
            recommended_item = torch.argmin(distance).item()

            anime_id = aidx_controller.get_anime_id(recommended_item)

            recommended_items.append(anime_id)

        return recommended_items
