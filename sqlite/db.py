from dotenv import load_dotenv
import sqlite3
import decimal
import json
import os

load_dotenv() #Load variables from .env file to environment
db = os.getenv("DB_PATH")

def create_connection():
    """ create a database connection to the SQLite database  
        path specified in .env file
    """
    conn = None
    try:
        conn = sqlite3.connect(db)
    except:
        print("Error connection not established")
    return conn

def dec_serializer(o):
    if isinstance(o, decimal.Decimal):
        return float(o)

def insert_humidity(hum):
    """
    Create a new entry into the HUMIDITY table
    :param hum(ambient humidity, location, and datetime):
    :return: humidity id
    """
    conn = create_connection()
    sql = ('insert into humidity values(?,?,?,?)')
    cur = conn.cursor()
    cur.execute(sql, hum)
    conn.commit()
    rowid = cur.lastrowid
    conn.close()
    print(rowid)
    return()

def insert_ltemp(ltemp):
    """
    Create a new entry into the LTemp table
    :param ltemp(liquid temperature, location, and datetime):
    :return: id
    """
    conn = create_connection()
    sql = ('insert into ltemp values(?,?,?,?)')
    cur = conn.cursor()
    cur.execute(sql, ltemp)
    conn.commit()
    conn.close()
    return()

def insert_atemp(atemp):
    """
    Create a new entry into the ATemp table:
    :param atemp(ambient temperature, location, and datetime):
    :return: id
    """
    conn = create_connection()
    sql = ('insert into atemp values(?,?,?,?)')
    cur = conn.cursor()
    cur.execute(sql, atemp)
    conn.commit()
    conn.close()
    return()

def insert_ec(ec):
    """
    Create a new entry into the ec table
    :param ec(electric conductivity, location, and datetime):
    :return: id
    """
    conn = create_connection()
    sql = ('insert into ec values(?,?,?,?)')
    cur = conn.cursor()
    cur.execute(sql, ec)
    conn.commit()
    conn.close()
    return()

def insert_ph(ph):
    """
    Create a new entry into the ph table
    :param ph(pH, location, and datetime):
    :return: id
    """
    conn = create_connection()
    sql = ('insert into ph values(?,?,?,?)')
    cur = conn.cursor()
    cur.execute(sql, ph)
    conn.commit()
    return()

def select_all_humidity():
    conn = create_connection()
    print(conn)
    cur = conn.cursor()
    cur.execute("SELECT * FROM humidity")
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return(json.dumps(rows))

def select_all_atemp():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM atemp")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))

def select_all_ph():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ph")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))

def select_all_ec():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ec")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))

def select_all_ltemp():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ltemp")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))

def select_all_openweather():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM OpenWeather")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))


def select_all_observations():
    """
    Query all rows in the table
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM OBSERVATIONS")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))

def select_all_sunhours():
    """
    Query all rows in the table
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM SUNHOURS")
    rows = cur.fetchall()
    conn.close()
    return(json.dumps(rows))

def store_sunhours(sunhours):
    """
         date              REAL PRIMARY KEY NOT NULL,
         sunrise           REAL NOT NULL,
         sunset            REAL NOT NULL,
         solarnoon         REAL NOT NULL,
         daylength         TEXT NOT NULL
    """
    conn = create_connection()
    sql = ('insert into sunhours values (?,?,?,?,?)')
    cur = conn.cursor()
    try:
        cur.execute(sql, sunhours)
        conn.commit()
        conn.close()
        return("Values successfully stored in DB.")
    except sqlite3.Error as e:
        print("Error Inserting Sunhours", e)
        return ("Error Inserting Sunhours", e)

def store_observations(observations):
    """
    OBSERVATIONS Table Columns:
         date            TEXT PRIMARY KEY    NOT NULL,
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
    """
    conn = create_connection()
    sql = ('insert into observations values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)')
    cur = conn.cursor()
    try:
        cur.execute(sql, observations)
        conn.commit()
        val = (cur.execute("SELECT * FROM OBSERVATIONS"))
        conn.close()
        return val
    except sqlite3.Error as e:
        print("Error Inserting Observations", e)
        return ("Error Inserting Observations", e)

""" 
        1 ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        2 descrip TEXT NULL,
        3 mdescrip TEXT NULL,
        4 feels_like REAL NULL,
        5 humidity REAL NULL,
        6 pressure REAL NULL,
        7 temperature REAL NULL,
        8 temp_max REAL NULL,
        9 temp_min REAL NULL,
        10 winddeg REAL NULL,
        11 windspeed REAL NULL,
        12 clouds REAL NULL,
        13 dt datetime REAL NULL
"""

def store_openWeather(weather):
    conn = create_connection()
    sql = ('insert into OpenWeather values (?,?,?,?,?,?,?,?,?,?,?,?,?)')
    cur = conn.cursor()
    try:
        cur.execute(sql, weather)
        conn.commit()
        val = (cur.execute("SELECT * FROM OpenWeather"))
        conn.close()
        return val
    except sqlite3.Error as e:
        print("Error Inserting OpenWeather Data", e)
        return ("Error Inserting OpenWeather Data", e)

def check_latest_observation():
    conn = create_connection()
    sql = ('SELECT date FROM OBSERVATIONS ORDER BY date(date) DESC Limit 1')
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return(rows)
    except sqlite3.Error as e:
        print("Error Checking Latest Observations Date", e)
        return ("Error Checking Latest Observations Date", e)

def check_latest_suntime():
    conn = create_connection()
    sql = ('SELECT date FROM SUNHOURS ORDER BY date(date) DESC Limit 1')
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return(rows)
    except sqlite3.Error as e:
        print("Error Checking Latest Sunhour Date", e)
        return ("Error Checking Latest Sunhour Date", e)
        
"""
w['weather'][0]['description'] test
w['weather'][0]['main']
w['main']['feels_like']
w['main']['humidity']
w['main']['pressure']
w['main']['temp']
w['main']['temp_max'] 
w['main']['temp_min'] 
w['wind']['deg']  
w['wind']['speed'] 
w['clouds']['all'] 
w['dt'] 
w['sys']['sunrise'] 
w['sys']['sunset']
"""
