import pymongo
import csv
import json
from backend.DBUserController import DBUserController

class DBController:
    def __init__(self):
        self.errorlog = "backend\\errorlog.txt"
        self.client = pymongo.MongoClient("mongodb+srv://AniMeAdmin:Haikyu!@cluster0.zhz9r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client.app
        self.userDB = DBUserController(self.errorlog, self.client, self.db)

    def get_animes(self):
        return self.db.anime

    # Helper method that attempts to return the given string as a number
    # It starts off with turning it into an int, then a double, and then a string
    # if all else fails
    def as_number(self, number):
        if (len(number) == 0):
            return None
        try:
            return int(number)
        except Exception as e:
            try:
                return float(number)
            except Exception as ex:
                return number

    # This method will go through a row in a table and turns it into a dictionary
    # object that can be inserted into the database
    def row_to_anime(self, row, column_names):
        anime = {}
        for i in range(0, len(row)):
            # we need to process areas where input could be an array
            if (len(row[i]) >= 2 and row[i][0] == "[" and row[i][len(row[i]) - 1] == "]"):
                # Get rid of quotes surrounding each element
                row[i] = row[i].replace("'", "")
                # Get rid of array brackets
                row[i] = row[i][1:len(row[i]) - 1]
                # Split into a list of strings based on each comma
                anime[column_names[i]] = row[i].split(",")
                # Strip extra spaces off each element and try to
                # get the proper type
                for j in range(0, len(anime[column_names[i]])):
                    anime[column_names[i]][j] = self.as_number(anime[column_names[i]][j].strip())
            else:
                anime[column_names[i]] = self.as_number(row[i])
        return anime

    # Takes an anime dictionary object and inserts it into the database
    def insert_anime_to_db(self, anime):
        try:
            self.db.anime.insert_one(anime)
            return True
        except Exception as e:
            # If there are any errors inserting the specified anime, log and
            # print it
            if (self.db.anime.count_documents({"Anime_id":anime["Anime_id"]}, limit = 1) == 0):
                print("Anime_id {} failed validation, writing to {}".format(anime["Anime_id"], self.errorlog))
                with open(self.errorlog, 'a') as log:
                    log.write("{}".format(anime))
                return False

    # Takes a csv file containing a dataset of animes and inserts it into the database
    def import_csv_animes(self, csv_path):
        with open (csv_path, encoding = 'UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            column_names = []
            for row in csv_reader:
                anime = None
                # If this is the first row, get the column names
                if index == 0:
                    column_names = row
                else:
                    anime = self.row_to_anime(row, column_names)
                index += 1

                # if this is an anime entry, insert it into the anime db
                if (anime != None and index > 0 and len(anime) == len(column_names)):
                    self.insert_anime_to_db(anime)

    def import_animes(self):
        self.import_csv_animes("C:\\Users\\jason\\Documents\\491B_AniMe\\app\\backend\\dataset.csv")
