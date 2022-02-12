#!/usr/bin/python
import sqlite3
import os

os.system('sudo touch greatsage.db')

conn = sqlite3.connect('greatsage.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE SUNHOURS
         (date             TEXT PRIMARY KEY NOT NULL,
         sunrise           REAL NOT NULL,
         sunset            REAL NOT NULL,
         solarnoon         REAL NOT NULL,
         daylength         TEXT NOT NULL);''')

print("Sunhours created successfully")

conn.execute('''CREATE TABLE EC
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         ec           REAL NOT NULL,
         location     TEXT NOT NULL,
         date         REAL NOT NULL   );''')

print("EC Table created successfully")

conn.execute('''CREATE TABLE PH
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         ph           REAL NOT NULL,
         location     TEXT NOT NULL,
         date         REAL NOT NULL   );''')

print("pH Table created successfully")

conn.execute('''CREATE TABLE LTemp
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         ltemp           REAL NOT NULL,
         location       TEXT NOT NULL,
         date         REAL NOT NULL   );''')

print("LTemp Table created successfully")

conn.execute('''CREATE TABLE HUMIDITY
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         hum           REAL NOT NULL,
         location      TEXT NOT NULL,
         date         REAL NOT NULL   );''')

print("HUMIDITY Table created successfully")

conn.execute('''CREATE TABLE ATemp
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         atemp           REAL NOT NULL,
         location     TEXT NOT NULL,
         date         REAL NOT NULL   );''')

print("ATemp Table created successfully")

conn.execute('''CREATE TABLE OBSERVATIONS 
         (
         ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         date            REAL NOT NULL,
         textDescription TEXT NULL,
         temp            REAL NULL,
         dewpoint        REAL NULL,
         windDirection   REAL NULL,
         windSpeed       REAL NULL,
         windGust        REAL NULL,
         barometricPressure REAL NULL,
         seaLevelPressure   REAL NULL,
         visibility         REAL NULL,
         maxTemp24          REAL NULL,
         minTemp24          REAL NULL,
         precipHour         REAL NULL,
         precip3            REAL NULL,
         precip6            REAL NULL,
         relativeHumidity   REAL NULL,
         windChill          REAL NULL,
         heatIndex          REAL NULL,
         cloudLayerSCT      REAL NULL,
         cloudLayerOVC      REAL NULL   );''')
print("Observations created successfully")

conn.execute('''CREATE TABLE OpenWeather 
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        descrip TEXT NULL,
        mdescrip TEXT NULL,
        feels_like REAL NULL,
        humidity REAL NULL,
        pressure REAL NULL,
        temperature REAL NULL,
        temp_max REAL NULL,
        temp_min REAL NULL,
        winddeg REAL NULL,
        windspeed REAL NULL,
        clouds REAL NULL,
        dt datetime REAL NULL
         );''')
print("Openweather table created successfully")

conn.close()