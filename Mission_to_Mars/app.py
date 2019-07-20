# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask app
app = Flask(__name__)

#Use flask_pymongo to set up connection through mLab
app.config["MONGO_URI"] = os.environ.get('authentication')
mongo = PyMongo(app)

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Scrape Route to Import `scrape_mars.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
    app.run()