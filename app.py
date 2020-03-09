# New Flask app to serve up 'Mission to Mars' website
# Imports
from flask import Flask, render_template, redirect
from flask import request
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import scrape_mars

#Create Flask instance
app = Flask(__name__)

#Establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

#Connect to/create database
# db = client.scraped_data_db
# collection = db.mars_data

# #Add data
# db.collection.insert_many ({
#         mars_data
#     })

# print("Connected")

# Create route to render html template
@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    # print(mars_data)
    
    return "<h3>Running ... please wait ...</h3>"
    return render_template("index.html", mars_data = mars_data)


@app.route("/scrape")   
def scrape():
    #Run scrape function
    mars_data = scrape_mars.scrape_mars_news()

    #Update db
    mongo_db_collection.update({scraped_data}, mars_data, upsert=True )

    #Return to home pg
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
