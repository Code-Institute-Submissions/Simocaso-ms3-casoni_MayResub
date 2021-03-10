from config import app
import os
from user import routes
from flask import (
    Flask, render_template, url_for)
# redirect, request, session,
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

# set to false before DEPLOYMENT!