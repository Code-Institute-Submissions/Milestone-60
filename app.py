import os, datetime, re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Global Variables
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'recruitment'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster.tzpih.mongodb.net/recruitment?retryWrites=true&w=majority'

mongo = PyMongo(app)




@app.route('/')
def home():
    recent_resumes=mongo.db.recipes.find().sort([("date",-1)]).limit(4)
    
    return render_template("home.html", recent_resumes=recent_resumes)

@app.route('/add_resume')
def add_resume():
    return render_template('add_resume.html', resumes=mongo.db.job_sector_title.find().sort([("name", 1)]))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)