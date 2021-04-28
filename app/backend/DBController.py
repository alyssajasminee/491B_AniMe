import pymongo
import ssl
import csv
import json
from backend.DBAnimeController import DBAnimeController
from backend.DBReviewController import DBReviewController
from backend.DBUserController import DBUserController
from backend.DBUserIdxController import DBUserIdxController
from backend.DBAnimeIdxController import DBAnimeIdxController

# This class aggregrates all the db controllers as well as provides general
# purpose utility functions
class DBController:
    def __init__(self):
        self.errorlog = "backend\\errorlog.txt"
        self.client = pymongo.MongoClient("mongodb+srv://AniMeAdmin:Haikyu!@cluster0.zhz9r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.client.app
        self.userDB = DBUserController(self.errorlog, self.client, self.db)
        self.reviewDB = DBReviewController(self.errorlog, self.client, self.db)
        self.animeDB = DBAnimeController(self.errorlog, self.client, self.db)
        self.userIdxDB = DBUserIdxController(self.errorlog, self.client, self.db)
        self.animeIdxDB = DBAnimeIdxController(self.errorlog, self.client, self.db)
