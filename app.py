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
   
    return render_template("home.html", recently_added_recipes=recently_added_recipes, most_viewed_recipes=most_viewed_recipes)
    

@app.route('/add_cv/<cv_id>')
def get_form(cv_id):
   
    return render_template('get_form.html', recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

