from flask import Flask, jsonify, request
from passlib.hash import pdkdf2_sha256
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
        
        #it return a json file
        return jsonify(user), 200