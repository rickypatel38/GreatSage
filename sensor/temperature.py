import os
import logging
import datetime

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

# Temperature Sensor 1-Wire Pullup Support
def load_kernel_modules():
	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folders = [d for d in os.listdir(base_dir) if d.startswith('28')]
if not device_folders:
	logging.error("No device folders found in {}".format(base_dir))
	sys.exit(1)
device_folder = device_folders[0]
device_file = os.path.join(base_dir, device_folder, 'w1_slave')
if not os.path.exists(device_file) or not os.access(device_file, os.R_OK):
	logging.error("Cannot access device file {}".format(device_file))
	sys.exit(1)
device_id = device_folder.split('/')[0]
last_read_time = datetime.datetime.utcnow()
cached_temp = None

def read_temp_raw():
	with open(device_file, 'r') as f:
		lines = f.readlines()
	if lines[0].strip()[-3:] == 'YES':
		equals_pos = lines[1].find('t=')
		if equals_pos != -1:
			temp = lines[1][equals_pos+2:]
			return temp


def calculate_temp(temp):
	return float(temp) / 1000.0

def read_temperature():
	global last_read_time
	global cached_temp
	now = datetime.datetime.utcnow()
	if (now - last_read_time).total_seconds() > 60 or cached_temp is None:
		# Read temperature from sensor if it has been more than 60 seconds since the last reading, or if no data has been cached
		temp = read_temp_raw()
		if temp is not None:
			temp_c = calculate_temp(temp)
			date = str(now)
			logging.debug("Liquid Temperature:{}, Date:{}".format(temp_c, date))
			print ("Liquid Temperature:",  temp_c)
			last_read_time = now
			cached_temp = temp_c
			return cached_temp
		else:
			# Handle the case where read_temp_raw returns None
			print("Error: Could not read temperature from sensor")
			logging.error("Error: Could not read temperature from sensor, Date:{}".format(date))
	else:
		# Use cached temperature data if it is less than 60 seconds since the last reading
		temp_c = cached_temp
		print("Using cached temperature data:", temp_c)
		return temp_c
