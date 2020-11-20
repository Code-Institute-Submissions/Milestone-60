import os, datetime, re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Global Variables
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'recruitment'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster.tzpih.mongodb.net/recruitment?retryWrites=true&w=majority'

mongo = PyMongo(app)
pg_lim = 8
first_pg = 1


@app.route('/')
def home():
    recently_added_resumes=mongo.db.resumes.find().sort([("date",-1)]).limit(4)
    return render_template("home.html", recently_added_resumes=recently_added_resumes)
    


@app.route('/add_resume')
def add_resume():
    return render_template('add_resume.html', job_title=mongo.db.job_title.find().sort([("job_sector_title", 1)]))



@app.route('/save_resume', methods=["POST"])
def save_resume():   
    resume=request.form.to_dict()
    resume["date"]=datetime.datetime.now()
    mongo.db.resumes.insert_one(resume)
    return redirect(url_for("get_resume"))


@app.route('/insert_resume', methods=["POST"])
def insert_resume():

    resume=request.form.to_dict()
    resume["date"]=datetime.datetime.now()
    mongo.db.resumes.insert_one(resume)
    return redirect(url_for("get_resumes"))




@app.route('/edit_resume/<resume_id>')
def edit_resume(resume_id):
    return render_template('edit_resume.html', resume=mongo.db.resumes.find_one({'_id': ObjectId(resume_id)}), job_title=mongo.db.resumes.find().sort([("name", 1)]))



@app.route('/resumes/<resume_id>/delete', methods=["POST"])
def delete_resume(resume_id):

    mongo.db.resumes.remove({'_id': ObjectId(resume_id)})
    return redirect(url_for('get_resumes'))


@app.route('/resume/<resume_id>')
def get_resume(resume_id):

    mongo.db.resumes.update_one({'_id': ObjectId(resume_id)}, {"$inc":{"clicks": 1}})
    return render_template('resume.html', resume=mongo.db.resumes.find_one({'_id': ObjectId(resume_id)}))



@app.route('/resumes')
def get_resumes():
    search=request.args.get('search')
    page = request.args.get('page')
    if not page:
        return redirect('/resumes?page=1')
    try:
        page = int(page)
    except (TypeError, ValueError):
        return redirect('/resumes?page=1')
    query={} if not search else {'name':re.compile(rf'{search}',re.I)}
    count=mongo.db.resumes.count(query)
    resumes=mongo.db.resumes.find(query)
    previous_url=url_for('get_resumes', page=page-1, search=search) if page > first_pg else None
    next_url=url_for('get_resumes', page=page+1, search=search) if page*pg_lim < count else None

    return render_template('resumes.html', resumes=resumes.sort([("date",-1)]).skip((page-first_pg)*pg_lim if page > first_pg else 0).limit(pg_lim), page=(page if count > pg_lim else None) if page > 0 else first_pg,  previous=previous_url, next=next_url, count=count)   


@app.route('/resumes/<resume_id>/update', methods=["POST"])
def update_resume(resume_id):
    
    mongo.db.resumes.update({'_id': ObjectId(resume_id)}, request.form.to_dict())
    return redirect(url_for('get_resume', resume_id=resume_id))

    




if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=False)
