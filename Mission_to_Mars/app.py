# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
from scrape_mars import scrape 
import os
import scrape_mars 


app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get('authentication')
mongo = PyMongo(app)

 
@app.route("/")
def home(): 

    
    mars_info = mongo.db.mars_info.find_one()

    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape(): 

    
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)