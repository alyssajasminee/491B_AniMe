import pymongo

class DBAnimeIdxController:
    def __init__(self, errorlog, client, db):
        self.errorlog = errorlog
        self.client = client
        self.db = db.anime_index

    def get_anime_id(self, new_anime_id):
        return self.db.find({'new_anime_id': new_anime_id})[0]['anime_id']

    def get_new_anime_id(self, anime_id):
        return self.db.find({'anime_id': anime_id})[0]['new_anime_id']
