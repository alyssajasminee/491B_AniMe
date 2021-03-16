from flask import Flask
from views import *
from backend.DBController import DBController

db = DBController()

def create_app(config_file):
	app = Flask(__name__)  # Create application object
	app.config.from_pyfile(config_file)  # Configure application with settings file, not strictly necessary

	#db.animeDB.drop_animes()
	#db.reviewDB.drop_reviews()
	#db.animeDB.import_csv_animes("backend/kaggle/dataset.csv")
	#db.reviewDB.import_csv_reviews("backend/kaggle/rating.csv")
	app.register_blueprint(home_view)  # Register url's so application knows what to do
	return app

if __name__ == '__main__':
	app = create_app('settingslocal.py')  # Create application with our config file
	app.run()  # Run our application
