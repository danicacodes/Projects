# Dependencies
import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# Define the Path to the hawaii.sqlite database located in the Resources folder
database_path = 'hawaii.sqlite?'
# Create an engine that can talk to the hawaii.sqlite database (using the database_path created above)
engine = create_engine(f'sqlite:///{database_path}',
    connect_args={'check_same_thread':False})
    

# Declare a Base using `automap_base()`which automatically 
# generates mapped classes and relationships from a database schema (typically the one which is reflected).
Base = automap_base()

# reflect hawaii.sqlite database into a new model and reflect the tables
Base.prepare(engine, reflect=True)

# Save references to both the Measurement and Station tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the sqlite database
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br>"
        f"-Dates and precipitation observations for Hawaii from the last year of the database (2016-08-23 to 2017-08-23).<br/>"
         f"<br/>"
        f"/api/v1.0/stations<br>"  
        f"-The weather stations for Hawaii.<br>"
        f"<br/>"
        f"/api/v1.0/tobs<br>"
        f"-Dates and temperature observations (tobs) for Hawaii from the last year of the database (2016-08-23 to 2017-08-23).<br>"
        f"<br/>"
        f"/api/v1.0/start<br/>"
        f"-List of temp_min, temp_avg and temp_max for Hawaii for all dates greater than and equal to the start date.<br>"
        f"<br/>"
        f"/api/v1.0/start/end<br/>"
        f"-List of temp_min, temp_avg and temp_max for Hawaii for all dates between start and end dates (inclusively).<br>"
        f"<br>"
        f"Example start date for start.<br>"
        f"/api/v1.0/2016-02-28<br>"
        f"<br>"
        f"Example of start and end date for start/end.<br>"
        f"/api/v1.0/2016-02-28/2016-03-05"
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    """Return precipitation observations for Hawaii from the last 12 months of the datebase"""
   
    # Find the last date in the database
    last_date_measurement = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date_measurement = last_date_measurement[0]

    # Calculate a date one year before the last date in the database
    one_year_ago = dt.datetime.strptime(last_date_measurement, '%Y-%m-%d') - dt.timedelta(days=365)        

    # Design a query to retrieve precipitation data for the last 12 months of precipatation data
    last_year_precipitation_results = session.query(Measurement.date, Measurement.station, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()

    last_year_precipitation = []
    for result in last_year_precipitation_results:
        prcp_dict = {}
        prcp_dict['date'] = result.date
        prcp_dict['station'] = result.station
        prcp_dict['prcp'] = result.prcp
        last_year_precipitation.append(prcp_dict)
    
    return jsonify(last_year_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of weather stations in Hawaii"""
    # Query to retrieve all stations from the hawaii.sqlite datebase
    # Return a JSON list of stations
    stations_results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    all_stations = []
    for result in stations_results:
        station_dict = {}
        station_dict['station'] = result.station
        station_dict['name'] = result.name
        station_dict['latitude'] = result.latitude
        station_dict['longitude'] = result.longitude
        station_dict['elevation'] = result.elevation
        all_stations.append(station_dict)
    
    return jsonify(all_stations)

@app.route("/api/v1.0/temperature")

def temperature():
    """Return temperature observations (tobs) for Hawaii from the last 12 months of the database"""     
    # Find the last date in the database
    last_date_measurement = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date_measurement = last_date_measurement[0]

    # Calculate a date one year before the last date in the database
    one_year_ago = dt.datetime.strptime(last_date_measurement, '%Y-%m-%d') - dt.timedelta(days=365)   
    
    # Design a query to retrieve temperature observations (tobs) for the last 12 months of database
    last_year_temp_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        filter(Measurement.date > one_year_ago).all()

    last_year_temp_list = []
    for temp_result in last_year_temp_results:
        temp_dict = {}
        temp_dict['date'] = temp_result[0]
        temp_dict['station'] = temp_result[1]
        temp_dict['tobs'] = float(temp_result[2])

        last_year_temp_list.append(temp_dict)

    return jsonify(last_year_temp_list) 

@app.route("/api/v1.0/<start>")

def temp_start_to_last_date(start = 'temp_start'):
    """Return temp_min, temp_avg and temp_max for Hawaii for all dates greater than and equal to the start date (till last date), or a 404 if not."""
    # Query to retrieve temperature observations for all dates greater than and equal to temp_start
      
    if start is None:
        return jsonify({"error": f"Please enter a start date"}), 404

    temp_start =  dt.datetime.strptime(start, "%Y-%m-%d").date() 
    temp_start_to_last_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        filter(Measurement.date >= temp_start).all()
    
    temp_start_to_last_list = []
    for temp_start_to_last_result in temp_start_to_last_results:
        temp_start_to_last_dict = {}
        temp_start_to_last_dict['date'] = temp_start_to_last_result[0]
        temp_start_to_last_dict['station'] = temp_start_to_last_result[1]
        temp_start_to_last_dict['tobs'] = float(temp_start_to_last_result[2])

        temp_start_to_last_list.append(temp_start_to_last_dict)
    return jsonify(temp_start_to_last_list)

@app.route("/api/v1.0/<start>/<end>")
  
def temp_start_to_end_date(start = 'temp_start_date', end = 'temp_end_date'):
    """Return temp_min, temp_avg and temp_max for Hawaii for all dates greater BETWEEN start and end dates (inclusively), or a 404 if not."""
    # Query to retrieve temperature observations for all dates BETWEEN <temp_start_date> and <temp_end_date> (inclusively)
    if start or end is None:
        return jsonify({"error": f"Please enter a start and/or end date"}), 404

    # Get the start date from the route
    temp_start_date =  dt.datetime.strptime(start, "%Y-%m-%d").date()

    # Get the end date from the route
    temp_end_date =  dt.datetime.strptime(end, "%Y-%m-%d").date()
    
    # Query to retrieve temperature observations for all dates BETWEEN <temp_start_date> and <temp_end_date> (inclusively)
    temp_start_to_end_date_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        filter(Measurement.date >= temp_start_date).\
        filter(Measurement.date <= temp_end_date).all()

    start_to_end_temp_list = []
    for result in temp_start_to_end_date_results:
        temp_start_to_end_dict = {}
        temp_start_to_end_dict['date'] = result[0]
        temp_start_to_end_dict['station'] = result[1]
        temp_start_to_end_dict['tobs'] = float(result[2])

        start_to_end_temp_list.append(temp_start_to_end_dict)

    return jsonify(start_to_end_temp_list) 


if __name__ == '__main__':
    app.run(debug=False)
