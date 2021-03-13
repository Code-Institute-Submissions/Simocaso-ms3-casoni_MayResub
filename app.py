import os
from config import app, mongo
from flask import (
    Flask, render_template, url_for, flash,
    redirect, request, session)
from functools import wraps

if os.path.exists('env.py'):
    import env

# Decorators; see here for more details: https://towardsdatascience.com/a-primer-on-args-kwargs-decorators-for-data-scientists-bb8129e756a7, https://stackoverflow.com/questions/49376371/python-decorators-args-and-kwargs
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

# set to false before DEPLOYMENT!