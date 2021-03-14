from flask import (
    redirect, request, session, jsonify)
from passlib.hash import pbkdf2_sha256
from config import mongo
import uuid


class User:

    # Method to start a session
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    # this function create the user object when signin in
    def signup(self):
        # print to debug during testing
        print(request.form)

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        
        # this instead, encrypts the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # this check if the user email already exist; flask jsonify: https://flask.palletsprojects.com/en/1.1.x/api/?highlight=jsonify#flask.json.jsonify#flask.json.jsonify
        if mongo.db.users.find_one({ "email": user['email']}):
            return jsonify({ "error": "This email address is already in use" }), 400

        # it return a json file; return jsonify(user), 200
        if mongo.db.users.insert_one(user):
            return self.start_session(user)

        # default response 
        return jsonify({ "error": "Invalid Signup"}), 400

    # sign out function
    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user = mongo.db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        
        return jsonify({"error": "Your Login credentials are invalid"}), 401


class Task:

    # Method to add a task
    def addTask(self):

        # class object
        task = {
            "_id": uuid.uuid4().hex,
            "new_task": request.form.get('add-task'),
            "complete_status": False 
        }

        mongo.db.tasks.insert_one(task)

        return jsonify(task), 200
