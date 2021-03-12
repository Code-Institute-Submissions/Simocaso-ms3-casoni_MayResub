from flask import render_template, url_for, flash, redirect, request, session
from bson.objectid import ObjectId
from config import app, mongo
# from user.models (folder/file) import User (class in the file)
from user.models import User
# from app (file/module) import app (instance of flask)
from app import app
from functools import wraps


# Decorators; see here for more details: https://towardsdatascience.com/a-primer-on-args-kwargs-decorators-for-data-scientists-bb8129e756a7, https://stackoverflow.com/questions/49376371/python-decorators-args-and-kwargs
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged in' in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")
    return wrap      


# routes
@app.route("/")
@app.route("/home")
def home():
    details = mongo.db.details.find()
    return render_template("pages/home.html", details=details)


@app.route("/signup", methods=["POST"])
def signup():
    return User().signup() 


@app.route("/signout")
def signout():
    return User().signout()     


@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template("pages/dashboard.html")


@app.route("/contact/")
def contact():
    return render_template("pages/contact.html")


# This route handles 404 errors
@app.errorhandler(404)
def invalid_route(e):
    return render_template('pages/404.html',  title="Page Not Found")