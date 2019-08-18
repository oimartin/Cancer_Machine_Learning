import os

import pandas as pd
import numpy as np
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, Float, String
from flask_cors import CORS
from flask import Flask, jsonify, render_template
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder, StandardScaler
from joblib import load
preprocess_pipeline = load('Model_Info/pipeline.joblib')
import pandas as pd
import numpy as np




app=Flask(__name__)
CORS(app)

raceList = pd.DataFrame({"races":["Black or African American", "White", "Asian or Pacific Islander"]})

stateList = pd.DataFrame({"states":["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", 
"NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI","WV", "WY"]})

genderList = pd.DataFrame({"genders":["Male","Female"]})

yearList = pd.DataFrame({"years":[1999.0,2000.0,2001.0,2002.0,2003.0,2004.0,2005.0,2006.0,2007.0,2008.0, 2009.0,2010.0,2011.0,2012.0,2013.0,2014.0,2015.0,2016.0,2017.0,2018.0,2019.0,2020.0,2021.0,2022.0,2023.0,2024.0,2025.0]})

cancerList = pd.DataFrame({"CancerType" : ["Larynx", "Lung", "Nasal", "Trachea"]})

pollutantList = pd.DataFrame({"pollutants": ["CO", "NO2","SO2","Ozeone","Lead","PM10","PM2_5"]})


def neuralNetwork(state,gender,race,year):
    print(state,gender,race)
    return {"lung": .024, "laryanx": .021, "nasal": .45, "trachea": .324}

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/<state>/<race>/<year>/<gender>")
def homeIndex(state,race,year,gender):
    from functions import NNpredict, getNNvalues
    values = getNNvalues(state,race,int(year),gender)
    results = NNpredict(values)
    return jsonify(results)
    del NNpredict
    

@app.route("/places")
def places():
    """Return a place names from database."""
    results = stateList['states']

    # Return a list of the column names (state names)
    return results.to_json(orient = 'records')

@app.route("/races")
def races():
    """Return a place names from database."""
    results = raceList['races']

    # Return a lit of the column names (race names)
    return results.to_json(orient = 'records')

@app.route("/genders")
def genders():
    """Return a place names from database."""
    results = genderList['genders']

    # Return a lit of the column names (gender names)
    return results.to_json(orient = 'records')

@app.route("/year")
def years():
    """Return a place names from database."""
    results = yearList['years']

    # Return a lit of the column names (year names)
    return results.to_json(orient = 'records')

@app.route("/machinelearn")
def machinelearn():
    return render_template("machinelearn.html")

@app.route("/visualization")
def analysis():
    return render_template("visualization.html")

if __name__ == "__main__":
    app.run(debug=True)