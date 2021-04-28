import pymongo

class DBUserIdxController:
    def __init__(self, errorlog, client, db):
        self.errorlog = errorlog
        self.client = client
        self.db = db.user_index

    def get_user_id(self, new_user_id):
        return self.db.find({'new_user_id': new_user_id})[0]['user_id']

    def get_new_user_id(self, user_id):
        return self.db.find({'user_id': user_id})[0]['new_user_id']
