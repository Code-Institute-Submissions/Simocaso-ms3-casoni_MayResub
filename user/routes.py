from flask import Flask
from config import app
# from user.models (folder/file) import User (class in the file)
from user.models import User
# from app (file/module) import app (instance of flask)
# from app import routes


@app.route("/signup", methods=["POST"])
def signup():
    return User().signup() 


@app.route("/signout")
def signout():
    return User().signout()  





