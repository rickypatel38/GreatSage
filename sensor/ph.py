import time
import datetime
import logging
import pylibftdi
from .atlas import AtlasDevice 
from .atlas import get_ftdi_device_list

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)
date = str(datetime.datetime.utcnow())


def read_tank_ph():
    # Only get the device list once, and store it in a variable
    devices = list(get_ftdi_device_list())
    input_val = 'R'
    dev = None
    for index in range(len(devices)):
        try:
            dev = AtlasDevice(devices[index])
            break
        except pylibftdi.FtdiError as e:
            logging.error("Failure: {}, Date:{}".format(e, date))
    if dev:
        dev.flush()
        try:
            dev.send_cmd(input_val)
            time.sleep(0.5)
            lines = dev.read_lines()
            ph = lines[0]
            pH = ph.replace('\r', '')
        except:
            logging.error("pH failure line 38, Date:{}".format(date))
        if pH is not None:
            print("pH:", pH)
            logging.debug("pH:{}, DateTime:{}".format(pH, date))
            return(pH)
        else:
            logging.error("pH Failure Line 41 Date:{}".format(date))
            print('Failed to get reading. Try again!')
    else:
        print("Device Not Found")
