## API LOGIC

import json

from predict import make_prediction

from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse


# from sklearn.linear_model import LinearRegression

# API INIT VARIABLES AND FUNCTIONS
app = Flask(__name__)
api = Api(app)


# Api response definition
class FlightDelayPredictor(Resource):
    # Com method definition
    def post(self):
        data = request.json
        output = make_prediction(data)
        return jsonify(output.tolist())


api.add_resource(FlightDelayPredictor, "/predict")

if __name__ == "__main__":

    app.run(debug=True)
