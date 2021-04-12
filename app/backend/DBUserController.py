import pymongo
import csv
import json
import random

u_id = "user_id"
user_key = "Username"
list_key = "AnimeList"
type_key = "Type"
email_key = "Email"
# This class is used to help faciliate any interface functions relating to users
# Mainly created to help make the logic more readable instead of stuffing DBController
class DBUserController:
    def __init__(self, errorlog, client, db):
        self.errorlog = errorlog
        self.client = client
        self.db = db

    def get_users(self):
        return self.db.user

    # This is a helper method that will help build queries for filtering users
    # currently only built with the username / user_id in mind
    def build_user_query(username=None, user_id=None):
        # if neither are provided, then we cannot query for whoever this function
        # is trying to find
        if username is None and user_id is None:
            return None;

        if username is not None:
            return {user_key:username}

        # if username is not provided, then user_id is
        return {u_id:user_id}


    # This function takes in the user's unique identifier and whether this user
    # should be an admin or not
    def set_admin(self, isAdmin, username=None, user_id=None):
        query = self.build_user_query(username=username, user_id=user_id)
        # Return early if we cannot query for this user
        if query is None:
            return

        # Figure out the type depending on isAdmin and set it to that new type
        type = "Admin";
        if not isAdmin:
            type = "User"

        update = {"$set": {"Type":type}}
        self.get_users().update(query, update)
        return

    def add_user(self, username, type, email):
        # modify user_id to be supplied in a better way to prevent clashes
        user_id = randint()

        user = {
            user_key: username,
            list_key: [],
            type_key: type,
            u_id: user_id,
            email_key: email
        }

        self.get_users().insert_one(user)

    def delete_user(self, username=None, user_id=None):
        query = self.build_user_query(username=username, user_id=user_id)
        if query is None:
            return

        self.get_users().delete_one(query)
