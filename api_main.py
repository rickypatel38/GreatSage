#!/usr/bin/env python3
from api_requests import getrequests
from sqlite import db
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  postgres_db  import postgres_calls
import sensor_main
import sqlite3
import os
import uvicorn
import json

load_dotenv() #Load variables from .env file to environment
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # SECURITY -- It is bad practice to allow * please change this to the approriate front-end endpoint only!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log_path = os.getenv("LOG_PATH") #pull the log path from .env file

@app.get("/getAllSensors")
def getAllSensors():
    return sensor_main.getAllSensors()

@app.get("/getAllHumidity")
def getHumidity():
    return db.select_all_humidity()

@app.get("/getAllEC")
def getEC():
    return db.select_all_ec()

@app.get("/getAllPH")
def getPH():
    return db.select_all_ph()

@app.get("/getAllATemp")
def getATemp():
    return db.select_all_atemp()

@app.get("/getAllLTemp")
def getLTemp():
    return db.select_all_ltemp()

@app.get("/getCurrentObservations/{zipcode}")
def current_obs(zipcode: int):
    checkObservationData(zipcode)
    return db.select_all_observations()

@app.get("/getSwitchOff/{outlet}")
def switchOff(outlet: int):
    return getrequests.getSwitchOff(outlet)

@app.get("/getSwitchOn/{outlet}")
def switchOn(outlet: int):
    return getrequests.getSwitchOn(outlet)

@app.get("/getSwitchStatus")
def switchStatus():
    return getrequests.getSwitchStatus
     

#42.582388, -83.151809
@app.get("/getHourlyData/{lat}/{lng}")
def get_hourly_data(lat: str, lng: str):
    logPath = log_path + "/hourly.json"
    getrequests.getHourlyForecast(lat, lng)
    with open(logPath) as f:
        data = json.load(f)
        return(data)

@app.get("/getAllHourly")
def select_all_hourly():
    logPath = log_path  + "/hourly.json"
    with open(logPath) as f:
        data = json.load(f)
        return(data)

@app.get("/getSunHours/{lat}/{lng}")
def get_sun_hours(lat: str, lng: str):
    #checkSunData(lat, lng)
    sunData = getrequests.getSunHours(lat, lng)
    postgres_calls.insert_sunhours(sunData)
    db.store_sunhours(sunData)
    return db.select_all_sunhours()

@app.get("/getOpenWeather/{lat}/{lng}")
def get_open_weather(lat: str, lng: str):
    v = getrequests.getOpenWeatherAPI(lat, lng)
    db.store_openWeather(v)
    postgres_calls.insert_openweather(v[1:])
    return db.select_all_openweather()

@app.get("/getWeeklyData/{lat}/{lng}")
def get_weekly_data(lat: str, lng: str):
    logPath = log_path + "/weekly.json"
    getrequests.getWeeklyForecast(lat, lng)
    with open(logPath) as f:
        data = json.load(f)
        return(data)
       
def checkObservationData(zipcode): #Checks to see if observational data in datasbase is up to date. If not it will fetch and then update the DB. 
    # get latest observation data from NOAA
    observationData = getrequests.getObservations(zipcode)
    dbObservationTime = db.check_latest_observation()

    if dbObservationTime == [] or dbObservationTime[0][0] != observationData[1]:
        db.store_observations(observationData)
    else:
        print("Already have the latest observation data from NOAA")
        return()
 
def checkSunData(lat, lng): #Checks to see if sunhours data in datasbase is up to date. If not it will fetch and then update the DB. 
    sunData = getrequests.getSunHours(lat, lng)
    dbLatestSunTime = db.check_latest_suntime()

    if dbLatestSunTime == [] or dbLatestSunTime[0][0] != str(sunData[0]):
        db.store_sunhours(sunData)
        postgres_calls.insert_sunhours(sunData)
    else:
        print("Already have sunrise and sunset times for today.")
        return()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    #Running on 0.0.0.0 instead of 127.0.0.1 allows it to be accessible on LAN rather than just on local machine only.