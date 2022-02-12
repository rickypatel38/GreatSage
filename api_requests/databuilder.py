import os
import time
from time import strptime
from calendar import timegm
from types import SimpleNamespace  
from datetime import datetime
from datetime import date


"""OBSERVATIONS Table Columns:
    id              int auto-crementing,
    date            REAL NOT NULL,
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
def create_observations(observation):
    v = 'value'
    o = SimpleNamespace(**observation)
    length = len(o.cloudLayers)
    if (length > 1):
        cloudlayers1  =  o.cloudLayers[1]['base'][v]
        observationData = (None, observationHourstoEpoch(o.timestamp), o.textDescription, o.temperature[v], o.dewpoint[v], o.windDirection[v], o.windSpeed[v], o.windGust[v], o.barometricPressure[v], o.seaLevelPressure[v], o.visibility[v], o.maxTemperatureLast24Hours[v], o.minTemperatureLast24Hours[v], o.precipitationLastHour[v], o.precipitationLast3Hours[v], o.precipitationLast6Hours[v], o.relativeHumidity[v], o.windChill[v], o.heatIndex[v], o.cloudLayers[0]['base'][v], cloudlayers1)
    else:
        observationData = (None, observationHourstoEpoch(o.timestamp), o.textDescription, o.temperature[v], o.dewpoint[v], o.windDirection[v], o.windSpeed[v], o.windGust[v], o.barometricPressure[v], o.seaLevelPressure[v], o.visibility[v], o.maxTemperatureLast24Hours[v], o.minTemperatureLast24Hours[v], o.precipitationLastHour[v], o.precipitationLast3Hours[v], o.precipitationLast6Hours[v], o.relativeHumidity[v], o.windChill[v], o.heatIndex[v], o.cloudLayers[0]['base'][v], None)
    return(observationData)

def create_weather(w):
    weather = (None, w['weather'][0]['description'], w['weather'][0]['main'], kelvinToCelsius(w['main']['feels_like']), w['main']['humidity'], w['main']['pressure'], kelvinToCelsius(w['main']['temp']), kelvinToCelsius(w['main']['temp_max']), kelvinToCelsius(w['main']['temp_min']), w['wind']['deg'],  w['wind']['speed'], w['clouds']['all'], w['dt'])
    return(weather)

def create_sun_hours(data): #converts all time to epoch time
    current_date = date.today()
    sunData = (current_date, sunHoursToEpoch(data['sunrise']), sunHoursToEpoch(data['sunset']), sunHoursToEpoch(data['solar_noon']), data['day_length'])
    return(sunData)

def sunHoursToEpoch(sunHours):
    fmt = ("%Y-%m-%d %I:%M:%S %p")
    today = datetime.today().strftime('%Y-%m-%d')
    fulltime = today +' '+ sunHours
    epochDate = int(timegm(strptime(fulltime, fmt)))    
    return epochDate

def observationHourstoEpoch(obsHours):
    obsHours = obsHours[:-6]
    timeFormat = '%Y-%m-%dT%H:%M:%S'
    unixTime = int(timegm(strptime(obsHours, timeFormat)))   
    return (unixTime)

def kelvinToCelsius(k):
   c = float(k-273.15)
   return(c)