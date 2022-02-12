from api_requests import databuilder #Formats Data then stores into SQLite DB. databuilder --> db.py
from api_requests import logmethods
from dotenv import load_dotenv
from noaa_sdk import noaa
import dlipower
import requests
import json
import os

load_dotenv() #Load variables from .env file to environment
n = noaa.NOAA()
api_key = os.getenv("API_KEY")
switch_key = os.getenv("DLI_PASS")
powerSwitch = "192.168.0.100"

def getWeeklyForecast(lat, lng):
    logmethods.writeToFile('weekly.json', n.points_forecast(lat, lng, hourly=False))
    logmethods.logTime()

def getHourlyForecast(lat, lng):
    logmethods.writeToFile('hourly.json', n.points_forecast(lat, lng, hourly=True))
    logmethods.logTime()

def getSunHours(lat, lng):
    urlString = "https://api.sunrise-sunset.org/json?lat="+lat+"&lng="+lng+"&date=today"
    r = requests.get(url=urlString)
    data = r.json()
    #return data['results'] uncomment for functional debugging.
    return (databuilder.create_sun_hours(data['results']))

def getOpenWeatherAPI(lat: str, lng: str):
    urlString = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lng+"&appid="+api_key
    r = requests.get(url=urlString)
    data = r.json()
    v = databuilder.create_weather(data)
    return (v)

def getForecast(zipcode):
    forecast = n.get_forecasts(postal_code=zipcode, country='US', hourly=True)
    return forecast

def getObservations(zipcode):
    observations = n.get_observations(zipcode,'US')
    for observation in observations:
        logmethods.writeToFile('observations.json', observation)
        if observation is not None:
            return(databuilder.create_observations(observation)) #store observationData into sqlitedb
        else:
            print("Service is down")
            return("Service is down")

def getSwitchOff(num):
    print('Connecting to a DLI PowerSwitch at 192.168.1.140')
    switch = dlipower.PowerSwitch(hostname=powerSwitch, userid="admin", password=switch_key)
    print('Turning OFF the outlet')
    switch.off(num)
    status = switch[num-1].state
    switch.session.close()
    return('The current status of Outlet:'+str(num)+ ' is: '+status)

def getSwitchOn(num):
    print('Connecting to a DLI PowerSwitch at 192.168.1.140')
    switch = dlipower.PowerSwitch(hostname=powerSwitch, userid="admin", password=switch_key)
    print('Turning ON the outlet')
    switch.on(num)
    status = switch[num-1].state
    switch.session.close()
    return('The current status of Outlet:'+str(num)+ ' is: '+status)

def getSwitchStatus(num):
    print('Connecting to a DLI PowerSwitch at 192.168.1.140')
    switch = dlipower.PowerSwitch(hostname=powerSwitch, userid="admin", password=switch_key)
    switchValues = switch
    switch.session.close()
    return('The current status of the powerswitch is:', switchValues)