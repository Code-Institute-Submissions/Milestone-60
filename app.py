import os, datetime, re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Global Variables
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'recruitment'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)

@app.route('/')
def home():
   
    return render_template("home.html")
    

@app.route('/add_recipe')
def add_recipe():
   
    return render_template('add_resume.html', resumes=mongo.db.job_sector_title.find().sort([("name", 1)]))