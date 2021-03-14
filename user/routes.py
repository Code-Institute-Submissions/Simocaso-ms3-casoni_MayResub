from config import app, mongo
from flask import Flask
# , request, url_for
# from user.models (folder/file) import User (class in the file)
from user.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup() 


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route("/user/login", methods=['POST'])
def login():
    return User().login() 

