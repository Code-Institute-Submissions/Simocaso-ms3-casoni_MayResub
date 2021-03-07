from flask import render_template, url_for, flash, redirect, request
from bson.objectid import ObjectId
from config import app

@app.route("/")
def home():
    details = mongo.db.details.find()
    return render_template("pages/home.html", details=details)


@app.route("/dashboard/")
def dashboard():
    return render_template("pages/dashborad.html")


# This route handles 404 errors
@app.errorhandler(404)
def invalid_route(e):
    return render_template('pages/404.html',  title="Page Not Found")