#import dependicies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Establish mongo connection
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Route to render index.html
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
