from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

#Establishing database connection
client = MongoClient()#insert connection string
db = client['vetnextdoor.vets'] #insert database name
collection = db['animals_accepted'] #put collection name

@app.route('/')
def home():
    print('<p>bonjour<p>') #make the homepage look pretty or sum pls (also add user input for query) 

@app.route('/search')
def search():
    for x in collection.find(animals_accepted:placeholder): #replace placeholder with user input (hypothetical front-end)
    print(x)