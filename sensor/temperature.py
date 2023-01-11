import os
import logging
import datetime


class TemperatureSensor:
    def __init__(self):
        logging.basicConfig(filename='logfile.log', level=logging.DEBUG)
        self.base_dir = '/sys/bus/w1/devices/'
        self.device_folders = [d for d in os.listdir(self.base_dir)
                               if d.startswith('28')]
        if not self.device_folders:
            logging.error('No device folders found in {}'.format(self.base_dir))
            sys.exit(1)
        self.device_folder = self.device_folders[0]
        self.device_file = os.path.join(self.base_dir,
                self.device_folder, 'w1_slave')
        if not os.path.exists(self.device_file) \
            or not os.access(self.device_file, os.R_OK):
            logging.error('Cannot access device file {}'.format(self.device_file))
            sys.exit(1)
        self.device_id = self.device_folder.split('/')[0]
        self.last_read_time = datetime.datetime.utcnow()

    def load_kernel_modules(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def read_temp_raw(self):
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        if lines[0].strip()[-3:] == 'YES':
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp = (lines[1])[equals_pos + 2:]
                return temp

    def calculate_temp(self, temp):
        return float(temp) / 1000

def read_temperature():
    sensor = TemperatureSensor()
    temp = sensor.read_temp_raw()
    if temp is not None:
        temp_c = sensor.calculate_temp(temp)
        date = str(datetime.datetime.utcnow())
        logging.debug('Liquid Temperature:{}, Date:{}'.format(temp_c, date))
        print ('Liquid Temperature:', temp_c)
        return temp_c
    else:
        print ('Error: Could not read temperature from sensor')
        logging.error('Error: Could not read temperature from sensor, Date:{}'.format(date))

