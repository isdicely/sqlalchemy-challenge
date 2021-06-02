# Import Dependencies
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

# reflect an existing database into a new model
    # creates set of clases for each table in hawaii.sqlite
Base = automap_base()

# reflect the tables (defines classes that represent data in the table)
Base.prepare(engine, reflect=True)

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

    return(

    )


if __name__ == '__main__':
    app.run()
