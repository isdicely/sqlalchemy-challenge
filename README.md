Climate Analysis and Exploration

In this challenge python Matplotlib, SQLAlchemy ORM queries and Flask was utilized to explore the API hawaii.sqlite to analyse the climate data within.

SQLAlchemy create_engine was used to connect to the sqlite database.
SQLAlchme automap_base() was used to reflect the tables in the database and save a reference to the clases Station and Measurement.
Python was linked to the database  by creating an SQLAlchemy session. 

Data analysis:
The precipitation data was analyzed as follows:
    Finding the most recent data in the data set
    Using this date to retreive the preceding 12 months of precipation data and dates.
    This information was loaded into a Pandas dataframe, plotted and conducted a statistical summary.
The Station data was used as follows:
    Query to calculate the total number of stations in the dataset.
    Query to find the most active station (station with most data rows).
    Utilizing the most active station calculating the lowest highest and average temperature recorded
Query on both datasets
    Retrive the last 12 months of temperature observations for the station with the most data.
    Plot the data as a histogram.


Climate App:
Utilizing the Flask library create the following routes:

/
    Home page/index including a list of all the routes avaiable

/api/v1.0/precipitation
    Returns a JSON represtaton of the dictionar that contains a query resulst of key value pairs of data:precipitation data


/api/v1.0/stations
    Return a JSON list of stations from the dataset.


/api/v1.0/tobs
    Query the dates and temperature observations of the most active station for the last year of data and return as a JSON list

/api/v1.0/<start> and /api/v1.0/<start>/<end>
    Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    Provided two sample queries to be used to access the API.