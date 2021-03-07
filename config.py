from flask import Flask
from os import path
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
if path.exists("env.py"):
    import env


# inizialization
app = Flask(__name__)
app.config["MONGODB_NAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)
   