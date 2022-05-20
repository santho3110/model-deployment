#!/usr/bin/env python
# coding: utf-8

# # Evaluate the Diabetes Dataset
# 
# The given dataset lists the glucose level readings of several pregnant women taken either during a survey examination or routine medical care. It specifies if the 2-hour post-load plasma glucose was at least 200 mg/dl. Analyze the dataset to:
# 
#     Find the features of the dataset
#     Find the response label of the dataset
#     Create a model  to predict the diabetes outcome
#     Use training and testing datasets to train the model
#     Check the accuracy of the model


#Import the required libraries
import joblib
import datetime

import numpy as np
import pandas as pd

from google.cloud import storage

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#Path to the training data source
DATA_PATH = "gs://alpha-buck/pima-indians-diabetes.data"
#Path to the model artifat
ARTIFACT_BUCKET = "gs://diabetes-artifacts"



#Use the .NAMES file to view and set the features of the dataset
feature_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']



#Use the feature names set earlier and fix it as the column headers of the dataset
diabetes_df = pd.read_csv(DATA_PATH, header=None, names=feature_names)



#Select features from the dataset to create the model
selected_features = ['pregnant', 'insulin', 'glucose', 'bmi', 'age']


#Create the feature object
x_feature = diabetes_df[selected_features]



#Create the reponse object
y_target = diabetes_df.label



#Split the dataset to test and train the model
x_train, x_test, y_train, y_test = train_test_split(x_feature, y_target, test_size=.25)



# Create a logistic regression model using the training set
logReg = LogisticRegression()
classifier = logReg.fit(x_train, y_train)



# Export the model to a file
model = 'model.joblib'
joblib.dump(classifier, model)

print('*'*100)
accuracy = accuracy_score(y_test, y_pred)
print("Succesfully trained model with accuracy ::", accuracy)

# Upload the model to GCS
bucket = storage.Client().bucket("retinapaty-artifacts")
blob = bucket.blob('{}/{}'.format(
    datetime.datetime.now().strftime('diabetes_%Y%m%d_%H%M%S'),
    model))
blob.upload_from_filename(model)

print("Uploded model artifacts to the destination.")
print('*'*100)
