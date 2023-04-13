
import pandas as pd
import numpy as np
import requests
import json

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
fligths_data = pd.read_csv("../data/all_features.csv", sep=",")

# filter columns
features = pd.concat([pd.get_dummies(fligths_data['OPERA'], prefix = 'OPERA'),pd.get_dummies(fligths_data['TIPOVUELO'], prefix = 'TIPOVUELO'), pd.get_dummies(fligths_data['MES'], prefix = 'MES')], axis = 1)
label = fligths_data['atraso_15']

# create train/test set 
X_train, X_test, y_train, y_test = \
    train_test_split(features, label, random_state=12)

# Serialize the data into json and send the request to the model
payload = {'data': json.dumps(X_test.tolist())}
y_predict = requests.post('http://127.0.0.1:5000/predict', data=payload).json()

# Make array from the list
y_predict = np.array(y_predict)
print(y_predict)