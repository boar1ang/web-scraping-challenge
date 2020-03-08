#Imports
from flask import Flask, render_template, redirect
from flask import request
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import scrape_mars
from bs4 import BeautifulSoup as bs4
import time

#Create Flask instance
app = Flask(__name__)

#Establish Mongo connection
mongo = PyMongo(app, url="mongodb://localhost:27017/mars_app")

# Create route to render html template & connect to db
@app.route("/")
def home():
    return "<h3>Running ...</h3>"
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", text="")


@app.route("/scrape")   
def scrape():
    #Run scrape function
    scraped_data = 

    #Update db
    mongo_db_collection

    #Return to home pg
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)