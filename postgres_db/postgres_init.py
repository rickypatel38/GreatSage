# Initialization Script for PostgresDB.
# This script creates tables for the PostgresDB.

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv() #Load variables from .env file to environment
host = os.getenv("POST_HOST")
database = os.getenv("POSTGRES")
user = os.getenv("POST_USER")
pw  = os.getenv("POST_PW")



def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host=host, database=database, user=user, password=pw, port=5432)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
       
def close(c): # close the communication with the PostgreSQL
    conn = c
    try:
        conn.cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE EC (
            id SERIAL PRIMARY KEY,
            ec REAL NOT NULL,
            location TEXT NOT NULL,
            date BIGINT NOT NULL
        )
        """,
        """ CREATE TABLE PH (
            id SERIAL PRIMARY KEY,
            ph REAL NOT NULL,
            location TEXT NOT NULL,
            date BIGINT NOT NULL
                )
        """,
        """
        CREATE TABLE LTemp (
            id SERIAL PRIMARY KEY,
            ltemp REAL NOT NULL,
            location TEXT NOT NULL,
            date BIGINT NOT NULL
        )
        """,
        """
        CREATE TABLE Humidity (
            id SERIAL PRIMARY KEY,
            hum REAL NOT NULL,
            location TEXT NOT NULL,
            date BIGINT NOT NULL
        )
        """,
        """
        CREATE TABLE ATemp (
            id SERIAL PRIMARY KEY,
            atemp REAL NOT NULL,
            location TEXT NOT NULL,
            date BIGINT NOT NULL
        )
        """,
        """
        CREATE TABLE SUNHOURS
         (date             TEXT PRIMARY KEY,
         sunrise           REAL NOT NULL,
         sunset            REAL NOT NULL,
         solarnoon         REAL NOT NULL,
         daylength         TEXT NOT NULL
         )
         """,
         """
         CREATE TABLE OpenWeather 
        (
        id SERIAL PRIMARY KEY,
        descrip TEXT,
        mdescrip TEXT,
        feels_like REAL,
        humidity REAL,
        pressure REAL,
        temperature REAL,
        temp_max REAL,
        temp_min REAL,
        winddeg REAL,
        windspeed REAL,
        clouds REAL,
        dt BIGINT
        )
        """,
        """
        CREATE TABLE OBSERVATIONS 
         (
         id SERIAL PRIMARY KEY,
         date            BIGINT NOT NULL,
         textDescription TEXT,
         temp            REAL,
         dewpoint        REAL,
         windDirection   REAL,
         windSpeed       REAL,
         windGust        REAL,
         barometricPressure REAL,
         seaLevelPressure   REAL,
         visibility         REAL,
         maxTemp24          REAL,
         minTemp24          REAL,
         precipHour         REAL,
         precip3            REAL,
         precip6            REAL,
         relativeHumidity   REAL,
         windChill          REAL,
         heatIndex          REAL,
         cloudLayerSCT      REAL,
         cloudLayerOVC      REAL 
         )
         """
        )
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = connect()
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
            print("Success: " + command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

create_tables()