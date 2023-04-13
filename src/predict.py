# imports
import os
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Environment variables

ARTIFACT_PATH = os.environ["ARTIFACT_PATH"]


# Helper functions
def load_artifacts(path):
    """Loads model artifact from path and returns
    features names and model params"""
    with open(path, "rb") as f:
        artifact = pickle.load(f)

    return artifact["model"], artifact["features_names"]

def encode_data(features_names, input_values):
    """Transform the input data to a hot-encoder one-row dataframe"""
    sample = pd.DataFrame(dict.fromkeys(features_names, 0.0), index=[0])
    for k, v in input_values.items():
        sample[f"{k}_{v}"] = 1.0
    sample = sample.fillna(0.0)

    return sample

def predict(model, input_data):
    """Returns model predictions"""
    return model.predict(input_data)

def make_prediction(input_values):
    """Main function for making predictions"""

    model, features_names = load_artifacts(ARTIFACT_PATH)

    input_data = encode_data(features_names=features_names,
                             input_values=input_values)
    
    return predict(model=model, input_data=input_data)



if __name__ == "__main__":

    test_data = {"OPERA": "Aerolineas Argentinas",
                 "TIPOVUELO": "I",
                 "MES": 12}

    print(make_prediction(test_data))
