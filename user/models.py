from flask import (
    Flask, render_template, url_for,
    redirect, request, session, jsonify)
from passlib.hash import pbkdf2_sha256
from config import mongo
import uuid


class User:

    def signup(self):

        # this function create the user object when signin in
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        
        # this instead, encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # this check if the user email already exist; flask jsonify: https://flask.palletsprojects.com/en/1.1.x/api/?highlight=jsonify#flask.json.jsonify#flask.json.jsonify

        # if mongo.db.users.find_one({ "email": user['email'] }):
        #    return jsonify({ "error": "Email address already in use" }), 400
        mongo.db.users.insert_one(user)

        #it return a json file
        return jsonify(user), 200