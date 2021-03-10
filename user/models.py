from flask import Flask, jsonify

class User:

    def signup(self):

        user = {
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }
        
        #it return a json file
        return jsonify(user), 200