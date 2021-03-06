from sensor import ec_sensor, t_sensor, ph_sensor, h_sensor #a_sensor
from sqlite import db
from postgres_db import postgres_calls
from dotenv import load_dotenv
import sqlite3
import time
import os

load_dotenv() #Load variables from .env file to environment
location = os.getenv("LOCATION") #Get location of sensors

def getEC():
    date = time.time()
    value = float(ec_sensor.read_tank_ec())
    ec = (None, value, location, date) #Format for inserting data into SQLite table.None is the ID Primary Key auto-incrementing and auto-generated by DB
    
    db.insert_ec(ec)
    postgres_calls.insert_ec(ec[1:]) #inserts the values from ec tuple without the leading "None" value for postgres.
    return value

def getPH():
    date = time.time()
    value = float(ph_sensor.read_tank_ph())
    ph =(None, value, location, date)
    
    db.insert_ph(ph)
    postgres_calls.insert_ph(ph[1:])
    return value

def getAmbient(): #new using a ds18b20
    date = time.time()
    #value = float(a_sensor.read_temp())
    #atemp = (None, value, location, date)
    
    #db.insert_atemp(atemp)
    #postgres_calls.insert_atemp(atemp[1:])
    #return (atemp)

def getLTemp():
    date = time.time()
    value = float(t_sensor.read_temp())
    ltemp = (None, value, location, date)
    
    db.insert_ltemp(ltemp)
    postgres_calls.insert_ltemp(ltemp[1:])
    return  value

def getHumidity():
    date = time.time()
    value = h_sensor.get_humidity()
    hum = (None, value, location, date)
    
    db.insert_humidity(hum)
    postgres_calls.insert_humidity(hum[1:])
    return (value)

def getAllSensors():
    ec = getEC()
    ph = getPH()
    ltemp = getLTemp()
    #atemp = getAmbient()
    #hum,atemp= getDHT22Ambient()
    date = time.time()
    print("Date:", date)
    #return (ec, ph, ltemp, atemp, date)
    return (ec, ph, ltemp, date)

getAllSensors()