import pymongo
import csv
import json
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
            log.write("{}\n".format(message))

    # Takes a csv file containing a dataset of anime ratings by users and inserts it
    # into the database as blank reviews
    # each row should contain user_id to anime_id plus a rating score
    def import_csv_reviews(self, csv_path):
        with open (csv_path, encoding = 'UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            column_names = []
            # maps anime ids to averages + num of reviews
            # this is so that we can update the rating on the animedb
            ratings = {}
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
                    # If it was successfully inserted, then update the rating for the
                    # relevant animes
                    self.insert_review_to_db(review, ratings)

            self.update_rating(ratings)

    # Inserts a review into the database
    def insert_review_to_db(self, review, ratings = None):
        # End early if this review does not review any existing animes in the database
        # log the ones that are not inserted
        if self.db.anime.count_documents({a_id:review[a_id]}, limit = 1) == 0:
            print("trying to review anime {} but it does not exist in the db".format(review[a_id]))
            self.write_to_errorlog(review, 'a')
            return False

        try:
            if desc_key not in review:
                review[desc_key] = ""
            if title_key not in review:
                review[title_key] = ""

            self.db.review.insert_one(review)
            print("User {} Submitted review of {} for anime {}".format(review[u_id], review[rating_key], review[a_id]))
            # Otimization choice. For larger operations it is more efficient
            # to provide this method with a ratings, that way we cut down
            # on the number of calls to update_ratings which each time will make
            # a call to the database
            if ratings is None:
                ratings = {}
                self.build_ratings(review, ratings)
                self.update_rating(ratings)
            else:
                self.build_ratings(review, ratings)
            return True
        except Exception as e:
            # If there are any errors inserting the specified review, log and
            # print it. Additionally checks to make sure this isn't a duplicated entry
            # in which case it just ignores it
            if (self.db.review.count_documents({u_id:review[u_id], a_id:review[a_id]}, limit = 1) == 0):
                print("review for user {} for anime {} failed validation, writing to {}"
                .format(review[u_id], review[a_id], self.errorlog))
                self.write_to_errorlog(review, 'a')
                return False
            else:
                print("user {} already has a review for anime {}"
                .format(review[u_id], review[a_id]))
                return False

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
    def build_ratings(self, review, ratings):
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
            if column_names[i] == u_id:
                review[column_names[i]] = row[i]
            else:
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
