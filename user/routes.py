from flask import render_template, url_for, flash, redirect, request
from bson.objectid import ObjectId
from config import app, mongo
# from app (file/module) import app (instance of flask)
from app import app
# from user.models (folder/file) import User (class in the file)
from user.models import User


# routes
@app.route("/")
@app.route("/home")
def home():
    details = mongo.db.details.find()
    return render_template("pages/home.html", details=details)


@app.route("/signup", methods=["GET"])
def signup():
    return User().signup() 
    # return render_template("pages/signup.html")


@app.route("/dashboard/")
def dashboard():
    return render_template("pages/dashboard.html")


@app.route("/contact/")
def contact():
    return render_template("pages/contact.html")


# This route handles 404 errors
@app.errorhandler(404)
def invalid_route(e):
    return render_template('pages/404.html',  title="Page Not Found")