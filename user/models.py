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

        mongo.db.users.insert_one(user)

        # this check if the user email already exist
        if mongo.db.user.find({ "email": user["email"]}):
            return jsonify({"error": "This email address is already in use"})

        #it return a json file
        return jsonify(user), 200