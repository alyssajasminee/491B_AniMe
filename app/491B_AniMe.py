from flask import Flask
from backend.DBController import DBController
from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import json_util
import json
from bson.objectid import ObjectId

db = DBController()
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGO_DBNAME'] = 'app'
app.config['MONGO_URI'] = 'mongodb+srv://AniMeAdmin:Haikyu!@cluster0.zhz9r.mongodb.net/app'
mongo = PyMongo(app)
users = mongo.db.user
animes = mongo.db.anime
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/genres', methods=['GET'])
def genres():
	g_list = []
	genres= ['Action','Adventure','Cars','Comedy','Dementia','Demons','Drama','Ecchi','Fantasy','Game','Harem','Hentai','Historical','Horror',
'Josei','Kids','Magic','Martial Arts','Mecha','Military','Music','Mystery','Parody','Police','Psychological','Romance','Samurai',
'School','Sci-Fi','Seinen','Shoujo','Shoujo Ai','Shounen','Shounen Ai','Slice of Life','Space','Sports','Super Power',
'Supernatural','Thriller','Vampire','Yaoi','Yuri']
	for j in genres:
		g=animes.find({"genre":j}).limit(7)
		output=[]
		myDocument = g.next() if g.next() else NULL
		i = 0
		while i < 5:
			if myDocument:
				output.append({"title":myDocument['title'], "type":myDocument['type'], "anime_id" : myDocument['anime_id']})
				myDocument = g.next()
			i+=1
		g_list.append({j:output})	
	return jsonify( g_list)

@app.route('/mypicks', methods=['GET'])
def my_list():
	u = users.find_one({"Username":"acervantes"})
	alist = u['AnimeList']
	output=[]
	
	for x in range(len(alist)):
		i = animes.find_one({"anime_id":alist[x]})
		output.append({"title":i['title'], "type":i['type'], "anime_id" : i['anime_id']})
	return jsonify( output)

@app.route('/anime/<int:animeId>', methods=['GET'])	
def iD(animeId):
	u = animes.find_one({"anime_id":animeId})
	output = [{"title":u['title'], "type":u['type'], "anime_id" : u['anime_id'],"synopsis" : u["synopsis"], "producer" : u["producer"], "studio" : u["studio"],
	"episodes" : u["episodes"], "aired" : u["aired"]}]
	return jsonify(output)

@app.route('/addAnime/<int:id>', methods=['GET','PATCH','OPTIONS'])
def addAnime(id):
	users.update({"Username":"acervantes"},{ '$addToSet': {"AnimeList": id}})
	return str(id)


@app.route('/RemoveAnime/<int:id>', methods=['GET','PATCH','OPTIONS'])
def RemoveAnime(id):
	users.update({"Username":"acervantes"},{'$pull':{"AnimeList": id}})
	return str(id)

if __name__ == '__main__':
	app.run()  # Run our application
