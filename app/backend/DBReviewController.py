import pymongo
import csv
import json
import datetime
from backend.DBUserController import DBUserController

a_id = "anime_id"
u_id = "user_id"
rating_key = "rating"
desc_key = "description"
title_key = "title"
scoredby_key = "scoredby"

class DBReviewController:
    def __init__(self, errorlog, client, db):
        self.errorlog = errorlog
        self.client = client
        self.db = db

    def get_reviews(self):
        return self.db.review

    # Function that builds the document for inserting into the database as opposed
    # to having to make it ourselves
    def add_review(self, user_id, anime_id, rating, description="", title=""):
        review = {}
        review[u_id] = user_id
        review[a_id] = anime_id
        review[rating_key] = rating
        review[desc_key] = description
        review[title_key] = title

        self.insert_reviews_to_db([review])

    # Function to find reviews for an anime
    def find_reviews(self, anime_id, min_rating=None, max_rating=None, size=10):
        query = {}
        query[a_id] = anime_id

        if min_rating or max_rating is not None:
            query[rating_key] = {}

        if min_rating is not None:
            query[rating_key]["$gt"] = min_rating

        if max_rating is not None:
            query[rating_key]["$lt"] = max_rating

        # make it so that we only find ratings that contain title and description
        query[title_key] = {"$ne":""}
        query[desc_key] = {"$ne":""}

        res = []
        for doc in self.get_reviews().find(query, limit=size):
            res.append(doc)

        return res

    # Debug function to remove all listed animes
    def drop_reviews(self):
        deleteCount = self.db.review.delete_many({})
        return deleteCount

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

    def write_to_errorlog(self, message, mode):
        with open(self.errorlog, mode) as log:
            log.write("\n{}\n{}\n".format(datetime.datetime.now(), message))

    # Takes a csv file containing a dataset of anime ratings by users and inserts it
    # into the database as blank reviews
    # each row should contain user_id to anime_id plus a rating score
    def import_csv_reviews(self, csv_path, batch_size = 10):
        with open (csv_path, encoding = 'UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            column_names = []
            # maps anime ids to averages + num of reviews
            # this is so that we can update the rating on the animedb
            ratings = {}
            # This is so we can send reviews in batches
            reviews = []
            for row in csv_reader:
                review = None
                # If this is the first row, get the column names
                if index == 0:
                    column_names = [col.lower() for col in row]
                    # if it isn't a review then report that the import csv
                    # operation failed
                    if not self.is_review(column_names):
                        print("Given csv file does not appear to contain reviews")
                        return False
                else:
                    review = self.row_to_review(row, column_names)
                index += 1

                # if this is a review entry, insert it into the anime db
                if (review != None and index > 0 and len(review) == len(column_names)):
                    reviews.append(review)

                # Check if we should send this batch yet
                if len(reviews) == batch_size:
                    self.insert_reviews_to_db(reviews, ratings)
                    # reset reviews
                    reviews = []

            # check if there are any leftover reviews to send
            if len(reviews) > 0:
                self.insert_reviews_to_db(reviews, ratings)

            self.update_rating(ratings)

    # Inserts a review into the database
    def insert_reviews_to_db(self, reviews, ratings = None):
        for review in reviews:
            if desc_key not in review:
                review[desc_key] = ""
            if title_key not in review:
                review[title_key] = ""

        try:
            self.db.review.insert_many(reviews, ordered = False)
            self.handle_ratings(reviews, ratings)
            print("Inserted {} reviews".format(len(reviews)))
        except Exception as writeErrors:
            # If there are any errors writing the reviews, then we should
            # log the errors
            failedWrites = set()
            for writeError in writeErrors.details["writeErrors"]:
                index = writeError["index"]
                failedWrites.add(index)
                review = reviews[index]
                errmsg = "User {} review for anime {} unsuccessfully inserted with message {}".format(review[u_id], review[a_id], writeError["errmsg"])
                print(errmsg)
                self.write_to_errorlog(errmsg, 'a')
            self.handle_ratings(reviews, ratings, failedWrites)
            print("Inserted {} reviews".format(len(reviews) - len(writeErrors.details["writeErrors"])))

    # Helper function to update the ratings for the related animes
    def handle_ratings(self, reviews, ratings = None, failedWrites = set()):
        # Keep track of whether or not we should write this change
        doWrite = ratings is None
        if ratings is None:
            ratings = {}
        # Reviews that were successfully inserted should update the ratings
        # for each anime
        for i in range(0, len(reviews)):
            if i not in failedWrites:
                self.build_rating(reviews[i], ratings)

        if doWrite:
            self.update_rating(ratings)

    # Helper function that iterates through the ratings dictionary to update
    # the ratings for each anime stored inside
    def update_rating(self, ratings):
        # Process the newly built ratings dictionary to update the ratings
        # for affected animes
        for key, value in ratings.items():
            query = {a_id:key}
            anime = self.db.anime.find_one(query)
            if anime is not None:
                rating = anime[rating_key] * anime[scoredby_key] + value[0]
                scoredby = anime[scoredby_key] + value[1]
                update = {"$set": {rating_key:rating / scoredby, scoredby_key:scoredby}}
                self.db.anime.update(query, update)

    # Helper function that helps build the ratings dictionary
    def build_rating(self, review, ratings):
        # Early return if review being inserted has a rating of -1 aka user
        # has watched but hasn't reviewed this anime
        if review[rating_key] < 0:
            return

        id = review[a_id]
        rating = [0, 0]
        if id in ratings:
            rating = ratings[id]

        # 0 is where we will accumulate the sum
        rating[0] += review[rating_key]
        # 1 is where we will accumulate how many ratings are stored
        rating[1] += 1

        ratings[id] = rating

    # Takes a row from a csv file and transforms it into a review dict object
    # to be inserted into the database
    def row_to_review(self, row, column_names):
        review = {}

        for i in range(0, len(row)):
            review[column_names[i]] = self.as_number(row[i])

        return review

    # helper function that determines whether or not something might be a review
    # from a csv file
    def is_review(self, column_names):
        if u_id not in column_names:
            return False
        if a_id not in column_names:
            return False
        if rating_key not in column_names:
            return False
        return True
