from config import app, mongo
from flask import Flask, request, url_for
# from user.models (folder/file) import User (class in the file)
from user.models import User
from app import dashboard



@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup() 


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route("/user/login", methods=['POST'])
def login():
    return User().login() 


@app.route("/add_task", methods=['POST'])
def add_task():
    task_item = request.form.get('add-task')
    # mongo.db.tasks-cl.insert_one({'text': add-task, })
    print(task_item)
    return redirect(url_for('dashboard'))
