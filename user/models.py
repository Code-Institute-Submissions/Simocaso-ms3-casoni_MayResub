from flask import flask, jsonify

class user:

    def signup(self):

        user = {
            "_id":"",
            "name":"",
            "email":"",
            "password":""
        }
    
    #it return a json file
    return jsonify(user), 200