import os
import glob
import logging
import datetime

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

#Temperature Sensor 1-Wire Pullup Support
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[1]
device_file = device_folder + '/w1_slave'
device_id = device_folder.split('/')[5]

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def calculate_temp(temp):
	return float(temp) / 1000.0

def read_temp():
	lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp=(lines[1][equals_pos+2:])
		temp_c = calculate_temp(temp)
		date = str(datetime.datetime.utcnow())
		logging.debug("Ambient Temperature:{}, Date:{}".format(temp_c, date))
		print ("Ambient Temperature:",  temp_c)
		return temp_c