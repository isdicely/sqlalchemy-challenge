# Import Dependencies
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up routes with Flask
app = Flask(__name__)

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
