from dns.rdataclass import NONE
from flask import Flask, request
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
review = mongo.db.review
CORS(app, resources={r'/*': {'origins': '*'}})


# GET ALL THE ANIMES BY GENRE
@app.route('/genres', methods=['GET'])
def genres():
	g_list = []
	genres= ['Action','Adventure','Cars','Comedy','Dementia','Demons','Drama','Ecchi','Fantasy','Game','Harem','Hentai','Historical','Horror',
'Josei','Kids','Magic','Martial Arts','Mecha','Military','Music','Mystery','Parody','Police','Psychological','Romance','Samurai',
'School','Sci-Fi','Seinen','Shoujo','Shoujo Ai','Shounen','Shounen Ai','Slice of Life','Space','Sports','Super Power',
'Supernatural','Thriller','Vampire','Yaoi','Yuri']
	for j in genres:
		g=animes.find({"genre":j}).limit(35)
		output=[]
		myDocument = g.next() if g.next() else NULL
		i = 0
		for i in g:
			
			output.append({"title":i['title'], "type":i['type'], "anime_id" : i['anime_id']})
				
		g_list.append({j:output})	
	return jsonify( g_list)



# GET THE USERS PERSONAL LIST OF ANIMES
@app.route('/mypicks', methods=['GET'])
def my_list():
	email = request.args.get('email')
	u = users.find_one({"Email": email})
	alist = u['AnimeList']
	mylist=[]
	
	for x in range(len(alist)):
		i = animes.find_one({"anime_id":alist[x]})
		mylist.append({"title":i['title'], "type":i['type'], "anime_id" : i['anime_id']})
	return jsonify( mylist)

# GET THE USERS username
@app.route('/userName', methods=['GET'])
def userName():
	email = request.args.get('email')
	u = users.find_one({"Email": email})
	return jsonify(u['Username'])

# GET ONE ANIMES' INFROMATION
@app.route('/anime/<int:animeId>', methods=['GET'])	
def iD(animeId):
	u = animes.find_one({"anime_id":animeId})
	output = [{"title":u['title'], "type":u['type'], "anime_id" : u['anime_id'],"synopsis" : u["synopsis"], "producer" : u["producer"], "studio" : u["studio"],
	"episodes" : u["episodes"], "aired" : u["aired"]}]
	return jsonify(output)



# ADD AN ANIME TO A USERS LIST 
@app.route('/addAnime', methods=['GET','PATCH','OPTIONS'])
def addAnime():
	anime_id = int(request.args.get('anime_id'))
	email = request.args.get('email')
	users.update({"Email":email},{ '$addToSet': {"AnimeList": anime_id}})
	return my_list()



# REMOVE AN ANIME FROM A USERS LIST
@app.route('/RemoveAnime', methods=['GET','PATCH','OPTIONS'])
def RemoveAnime():
	anime_id = int(request.args.get('anime_id'))
	email = request.args.get('email')
	users.update({"Email":email},{'$pull':{"AnimeList": anime_id}})
	return my_list()




# PUT A REVIEW FOR AN ANIME 
@app.route('/ReviewAnime', methods=['GET','POST'])
def ReviewAnime():
	anime_id = int(request.args.get('anime_id'))
	email = request.args.get('email')
	u = int(users.find_one({"Email": email})['user_id'])
	rating = int(request.args.get('rating'))
	doc= {"user_id":u, 'anime_id':anime_id, "rating": rating, "description":"", "title":""}
	review.insert_one(doc)


	return jsonify(rating)

# PUT A REVIEW FOR AN ANIME 
@app.route('/FindReview', methods=['GET'])
def FindReview():
	anime_id = int(request.args.get('anime_id'))
	email = request.args.get('email')
	u = users.find_one({"Email": email})['user_id']
	
	r = review.find_one({"anime_id":anime_id,"user_id":u})
	if r is None:
		return jsonify(0)

	return jsonify(r["rating"])

if __name__ == '__main__':
	app.run()  # Run our application
