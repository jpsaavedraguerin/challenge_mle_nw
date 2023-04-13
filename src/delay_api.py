## API LOGIC
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json

#from sklearn.linear_model import LinearRegression

# API INIT VARIABLES AND FUNCTIONS
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('input_data')

# Load model
model_params_path = "/media/sguerin/JPSG/02_Personal/01_Projects/09_Challenge_NW/API_NW/models/logreg.pkl"
with open(model_params_path, "rb") as f:
    model = pickle.load(f)

# Api response definition
class DelayPredictor(Resource):
    # Com method definition
    def post(self):
        args = parser.parse_args()
        input = np.array(json.loads(args['data']))
        output = model.predict(input)
        return jsonify(output.tolist())

api.add_resource(DelayPredictor, '/predict')

if __name__ == "__main__":
    # load model
    path = "/media/sguerin/JPSG/02_Personal/01_Projects/09_Challenge_NW/API_NW/models/logreg.pkl"
    with open(path, "rb") as f:
        model = pickle.load(f)


    app.run(debug=True)



