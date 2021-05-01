from config import app, mongo
from flask import Flask, redirect, url_for
from bson.objectid import ObjectId
import uuid
# from user.models (folder/file) import User (class in the file)
from user.models import User, Task


@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("pages/dashboard.html", tasks=tasks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("pages/dashboard.html", tasks=tasks)


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


@app.route('/complete/<taskId>')
def complete(taskId):
    new_task = mongo.db.tasks.find_one({'_id': taskId})
    new_task['complete_status'] = True
    mongo.db.tasks.save(new_task)
    return redirect(url_for('dashboard'))


@app.route('/delete_completed')
def delete_completed():
    mongo.db.tasks.delete_many({'complete_status': True})
    return redirect(url_for('dashboard'))


@app.route('/delete_all')
def delete_all():
    mongo.db.tasks.delete_many({})
    return redirect(url_for('dashboard'))
