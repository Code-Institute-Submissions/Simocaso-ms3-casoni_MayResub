from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid
from app import db

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

        db.user.insert_one(user)

        #it return a json file
        return jsonify(user), 200