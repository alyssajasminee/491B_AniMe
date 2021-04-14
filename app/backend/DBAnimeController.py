import pymongo
import csv
import json
import datetime

a_id = "anime_id"
title_key = "title"
genre_key = "genre"
synopsis_key = "synopsis"
type_key = "type"
producer_key = "producer"
studio_key = "studio"
rating_key = "rating"
scoredby_key = "scoredby"
popularity_key = "popularity"
members_key = "members"
episodes_key = "episodes"
source_key = "source"
aired_key = "aired"
link_key = "link"

class DBAnimeController:
    def __init__(self, errorlog, client, db):
        self.errorlog = errorlog
        self.client = client
        self.db = db

    # Debug function to remove all listed animes
    def drop_animes(self):
        deleteCount = self.db.anime.delete_many({})
        return deleteCount

    def get_animes(self):
        return self.db.anime

    def find_anime_by_popularity(self, min_popularity=0, max_popularity=None, min_rating=0, max_rating=None, size=10):
        query = {}
        query[popularity_key] = {}
        query[rating_key] = {}

        query[popularity_key]["$gt"] = min_popularity
        query[rating_key]["$gt"] = min_rating

        if max_popularity is not None:
            query[popularity_key]["$lt"] = max_popularity
        if max_rating is not None:
            query[rating_key]["$lt"] = max_rating

        anime = []
        for doc in self.get_animes().find(query, limit = size):
            anime.append(doc)

        return anime

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
    def insert_animes_to_db(self, animes):
        for anime in animes:
            # inserted animes should always start with a rating of 0 since we
            # don't have any users who have rated it yet
            anime[rating_key] = 0
            # make calculating rating easier / less resource intensive
            anime[scoredby_key] = 0

        try:
            self.db.anime.insert_many(animes, ordered = False)
            print("Inserted {} animes".format(len(animes)))
        except Exception as writeErrors:
            # If there are any errors writing the reviews, then we should
            # log the errors
            for writeError in writeErrors.details["writeErrors"]:
                index = writeError["index"]
                anime = animes[index]
                errmsg = "anime {} unsuccessfully inserted with message {}".format(anime[a_id], writeError["errmsg"])
                print(errmsg)
                self.write_to_errorlog(errmsg, 'a')

            print("Inserted {} animes".format(len(animes) - len(writeErrors.details["writeErrors"])))

    def write_to_errorlog(self, message, mode):
        with open(self.errorlog, mode) as log:
            log.write("\n{}\n{}\n".format(datetime.datetime.now(), message))

    # Takes a csv file containing a dataset of animes and inserts it into the database
    def import_csv_animes(self, csv_path, batch_size = 10):
        with open (csv_path, encoding = 'UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            column_names = []
            animes = []
            # This is to prevent csv files from having duplicated values which the main one we are using does smh
            seenIds = set()
            for row in csv_reader:
                anime = None
                # If this is the first row, get the column names
                if index == 0:
                    column_names = [col.lower() for col in row]
                else:
                    anime = self.row_to_anime(row, column_names)
                index += 1

                # if this is an anime entry, insert it into the anime db
                if anime != None and index > 0 and len(anime) == len(column_names) and anime[a_id] not in seenIds:
                    animes.append(anime)
                    seenIds.add(anime[a_id])

                if len(animes) == batch_size:
                    self.insert_animes_to_db(animes)
                    animes = []
            # After we are done reading the batch, send whatever is leftover
            self.insert_animes_to_db(animes)
