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
   

    recent_resumes=mongo.db.resumes.find().sort([("date",-1)]).limit(4)
    return render_template("home.html", recent_resumes=recent_resumes)

    
    return render_template("home.html", recent_resumes=recent_resumes)

@app.route('/add_resume')
def add_resume():
    return render_template('add_resume.html', resumes=mongo.db.resumes.job_sector_title.find().sort([("name", 1)]))



@app.route('/save_resume', methods=["POST"])
def save_resume():   
    resume=request.form.to_dict()
    resume["date"]=datetime.datetime.now()
    mongo.db.reumes.insert_one(resume)
    return redirect(url_for("get_resume"))


@app.route('/all_resumes/<resume_id>/delete', methods=["POST"])
def delete_resume(resume_id):
    mongo.db.resumes.remove({'_id': ObjectId(resume_id)})
    return redirect(url_for('get_resume'))



@app.route('/edit_resume/<resume_id>')
def edit_resume(resume_id):
    return render_template('edit_resume.html', resume=mongo.db.resumes.find_one({'_id': ObjectId(resume_id)}), job_title=mongo.db.resumes.job_sector_title.find().sort([("name", 1)]))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)
