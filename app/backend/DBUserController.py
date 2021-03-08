import pymongo
import csv
import json

# This class is used to help faciliate any interface functions relating to users
# Mainly created to help make the logic more readable instead of stuffing DBController
class DBUserController:
    def __init__(self, errorlog, client, db):
        self.errorlog = errorlog
        self.client = client
        self.db = db

    def get_users(self):
        return self.db.user

    # This function takes in the user's unique identifier and whether this user
    # should be an admin or not
    def set_admin(self, username, isAdmin):
        # Get document from MongoDB
        query = {"Username":username}

        # Figure out the type depending on isAdmin and set it to that new type
        type = "Admin";
        if not isAdmin:
            type = "User"

        update = {"$set": {"Type":type}}
        self.get_users().update(query, update)
        return
