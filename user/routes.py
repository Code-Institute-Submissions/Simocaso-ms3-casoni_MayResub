from config import app, mongo
from bson.objectid import ObjectId
from flask import Flask, redirect, url_for
import uuid
# , request, url_for
# from user.models (folder/file) import User (class in the file)
from user.models import User, Task


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup() 


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login() 


@app.route('/user/addTask', methods=['POST'])
def addTask():
    return Task().addTask()


@app.route('/marked/<oid>')
def marked(oid):
    task_item = mongo.db.tasks.find_one({'_id': uuid.uuid4().hex(ObjectId(oid))})
    task_item['complete_status'] = True
    mongo.db.tasks.save(task_item)
    return redirect(url_for('dashboard'))
