    
# setting up the dependencies

import os

import pandas as pd
import numpy as np
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, Float, String

from flask import Flask, jsonify, render_template
# from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/cancer_pollution_db.sqlite"
db = SQLAlchemy(app)

class Pollution(db.Model):
    __tablename__ = 'pollution_table'

    id = Column(Integer, primary_key=True)
    CO = Column(Float)
    County_Code = Column(Float)
    Lead = Column(Float)
    NO2 = Column(Float)
    Ozone = Column(Float)
    PM10 = Column(Float)
    PM2_5 = Column(Float)
    SO2 = Column(Float)
    State = Column(String)
    Year = Column(Integer)

    def __init__(id, self, CO, County_Code, Lead, NO2, Ozone, PM10, PM2_5,
                SO2, State, Year):
                self. id = id
                

    def __repr__(self):
        return '<Pollutant %r>' % (self.CO)

# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/test")
def list_pollutants():
    return jsonify(id=Column(Integer, primary_key=True)
    CO = Column(Float)
    County_Code = Column(Float)
    Lead = Column(Float)
    NO2 = Column(Float)
    Ozone = Column(Float)
    PM10 = Column(Float)
    PM2_5 = Column(Float)
    SO2 = Column(Float)
    State = Column(String)
    Year = Column(Integer))


if __name__ == "__main__":
    app.run(debug=True)
