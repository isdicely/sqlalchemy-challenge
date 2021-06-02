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
        f"<li>/api/v1.0/temp/start/end</li>"
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



if __name__ == '__main__':
    app.run()
