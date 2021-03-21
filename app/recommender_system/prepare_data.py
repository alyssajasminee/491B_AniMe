# !/usr/bin/python
import numpy as np
import pandas as pd

import app.backend.DBController as dbc
# from app.backend.DBController import DBController

def to_df(db, query, limit=None):
    if limit is None:
        cursor = db.find(query)
    else:
        cursor = db.find(query).limit(limit)

    df = pd.DataFrame(list(cursor))
    return df

if __name__ == "__main__":
    rdb_controller = dbc.DBController().reviewDB

    reviews_db = rdb_controller.get_reviews()

    df = to_df(reviews_db, {})

    print(df)

    # reviews_collection.find({'user_id': '1'})
    #
    # for x in reviews_db.distinct('anime_id'):
    #     print(x)
