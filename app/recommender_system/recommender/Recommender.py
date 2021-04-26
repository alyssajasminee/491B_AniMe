import yaml
import app.backend.DBController as dbc

from sklearn.neighbors import BallTree
from recommender_system.utils import *


class Recommender:
    def __init__(self):
        with open('../configs/config.yaml', 'r') as stream:
            self.settings = yaml.safe_load(stream)

        self.model_type = self.settings['MODEL']

        model_path = os.path.join('./models', self.model_type + '.pth')
        self.model_dict = get_model(self.settings, load_path=model_path)

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
        item_idxs = self.get_item_idxs(user_id)

        items = self.model_dict['model'].items(torch.LongTensor(item_idxs)).numpy()
        ball_tree = BallTree(items, leaf_size=33)

        query = self.model_dict['model'].users(torch.LongTensor([user_id])).numpy()

        _, idxs = ball_tree.query(query, k=k)

        recommended_items = []
        for idx in idxs:
            recommended_item = items[idx]

            distance = torch.norm(items.weight.data - recommended_item, dim=1)
            recommended_items.append(torch.argmin(distance).item())

        return recommended_items
