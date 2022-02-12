import sys
import json
import time
import socket
import logging
import datetime
import Adafruit_DHT

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)
date = str(datetime.datetime.utcnow())

sensor_type = Adafruit_DHT.DHT22
sensor_gpio = 23 #GPIO Pin location on Raspberry Pi

def json_structure(location, humidity, temperature, date):
	data = {}
	data['location'] = location
	data['humidity'] = humidity
	data['temperature'] = temperature
	data['datetime'] = date
	return json.dumps(data)


def read_ht():
	humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_gpio)
	if humidity is not None and temperature is not None:
		try:
			logging.debug("Room Humidity:{}, DateTime:{}".format(humidity, date))
			logging.debug("Room Temperature:{}, DateTime:{}".format(temperature, date))
			print ("Room Humidity:", humidity)
			print ("Room Temperature:", temperature)
			return(humidity,temperature)
		except:
			logging.error("Humidity Failure Line 33 Date:{}".format(date))
			print("unable to get data")
	if humidity is None or temperature is  None: 
		logging.error("Humidity Failure Line 36 Date:{}".format(date))
		print('temperature or humidity data is NULL')
