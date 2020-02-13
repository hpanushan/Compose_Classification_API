from flask import Flask, request
from flask_restful import Resource, Api
import json

from GetMatchedIntent import getMatchedIntent

app = Flask(__name__)
api = Api(app)

class New(Resource):
    def get(self):
        # Activation
        return {"similarPhrase":12}, 200

    def post(self):
        # Getting Post data
        post_json = request.get_json()

        # Convert JSON into Dictionary
        post_dict = json.loads(post_json)

        # Key values of post data
        user_input = post_dict['user_input']
        options = post_dict['options']

        return getMatchedIntent(user_input,options), 201

# Routes
api.add_resource(New,'/')

if __name__ == '__main__':
    app.run(port='5000',debug=True)