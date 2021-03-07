import os
from flask import Flask
from flask import pymongo
from bson.objectid import objectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGODB_NAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    return "home"
   

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # set to false before DEPLOYMENT!