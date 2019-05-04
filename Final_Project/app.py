    
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/cancer_pollution_db.sqlite"
db = SQLAlchemy(app)

class pollution(db.Model):
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
    return render_template("index.html", pollution=pollution)


# Query the database and send the jsonified results
@app.route("/test")
def list_pollutants():
    results = db.session.query(
        pollution.CO,
        pollution.County_Code,
        pollution.Lead,
        pollution.NO2,
        pollution.Ozone,
        pollution.PM10,
        pollution.PM2_5,
        pollution.SO2,
        pollution.State,
        pollution.Year
    ).\
        order_by(pollution.Year.desc())

#Create lits from the query results

    pollution_data = []
    for d in results[:15]:

        print('data:', d)

        pollution_data.append({
            "CO": d[0],
            "County_Code": d[1],
            "Lead": d[2],
            "NO2": d[3],
            "Ozone": d[4],
            "PM10": d[5],
            "PM2_5": d[6],
            "SO2": d[7],
            "State": d[8],
            "Year": d[9]
        })
# Generate the plot trace
    trace1 = {
        "x": ["CO","Lead","NO2","Ozone","PM10","PM2_5","SO2"],
        "y": pollution_data,
        #"y": [pollution.CO,pollution.Lead,pollution.NO2,pollution.Ozone,pollution.PM10,pollution.PM2_5,pollution.SO2],
        "type": "bar"
    }
    return jsonify(trace1)

    


    #return json.dumps(pollution_data)
    #return json.dumps(pollution_data)


if __name__ == "__main__":
    app.run(debug=True)
