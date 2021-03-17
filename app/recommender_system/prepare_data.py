# !/usr/bin/python
import app.backend.DBController as dbc
# from app.backend.DBController import DBController

if __name__ == "__main__":
    db_controller = dbc.DBController()
    # db_controller = DBController()

    anime_list = db_controller.get_animes()

    print(anime_list)