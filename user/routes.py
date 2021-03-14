from config import app, mongo
from flask import Flask, redirect
# , request, url_for
# from user.models (folder/file) import User (class in the file)
from user.models import User, Task


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup() 


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route("/user/login", methods=['POST'])
def login():
    return User().login() 


@app.route("/user/addTask", methods=['POST'])
def addTask():
    return Task().addTask()


@app.route("/marked/<oid>")
def marked(oid):
    return redirect(url_for('pages/dashboard.html'))
