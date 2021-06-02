# Import Dependencies
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, json, jsonify


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

# reflect an existing database into a new model
# creates set of clases for each table in hawaii.sqlite
Base = automap_base()

# reflect the tables (defines classes that represent data in the table)
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)
session


# Set up routes with Flask
app = Flask(__name__)

# Index route


@app.route("/")
def index():
    return(
        f"<h1>Hawaii Climate Analysis API</h1>"
        f"<p>Available Routes:"
        f"<ul>"
        f"<li>/api/v1.0/precipitation</li>"
        f"<li>/api/v1.0/stations</li>"
        f"<li>/api/v1.0/tobs</li>"
        f"<li>/api/v1.0/temp/&lt;start&gt;/&ltend&gt</li>"
        f"<ul> sample url: /api/v1.0/temp/2017-08-17 </ul>"
        f"</ul></p>"
    )

    # precipation route


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Find the most recent date in the data set.
    latest_date = dt.date.fromisoformat(
        session.query(func.max(Measurement.date)).first()[0])
    # Calculate the date one year from the last date in data set.
    earliest_date = latest_date.replace(year=latest_date.year - 1)
    # Perform a query to retrieve the data and precipitation scores
    data = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date >= earliest_date.isoformat()).all()
    result = {date: prcp for date, prcp in data}
    return jsonify(result)

    # station route


@app.route("/api/v1.0/stations")
def stations():
    # Design a query to calculate the total number stations in the dataset
    result = session.query(Station.station).all()
    return jsonify(result)

    # temperature observation route


@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most recent date in the data set.
    latest_date = dt.date.fromisoformat(
        session.query(func.max(Measurement.date)).first()[0])
    # Calculate the date one year from the last date in data set.
    earliest_date = latest_date.replace(year=latest_date.year - 1)
    # Design a query to find the most active stations (i.e. what stations have the most rows?)
    # List the stations and the counts in descending order.
    station_counts = session.query(Measurement.station, func.count(Measurement.station)).group_by(
        Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    # Using the most active station id
    # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
    temps_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == station_counts[0][0]).filter(
        Measurement.date >= earliest_date).all()
    result = {date: tobs for date, tobs in temps_results}
    return jsonify(result)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature 
    # for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/temp/<start>/<end>")
@app.route("/api/v1.0/temp/<start>")
def temp_info(start, end = None):
     
    # calculate the lowest, highest, and average temperature for a start or start/end dates
    query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(
        Measurement.date >= start)
    if end:
        query = query.filter(Measurement.date <= end)
    summary = query.all()[0]
    result = {"min_temp": summary[0], "avg_temp": summary[1], "max_temp": summary[2]}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
