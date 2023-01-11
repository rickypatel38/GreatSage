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
    devices = get_ftdi_device_list()

    # Use a for loop to iterate through the devices, rather than a while True loop
    for index in range(len(devices)):
        try:
            dev = AtlasDevice(devices[index])
            break
        except pylibftdi.FtdiError as e:
            logging.error("Failure: {}, Date:{}".format(e, date))

    time.sleep(1)
    dev.flush()
    try:
        input_val = 'R'
        # pass commands straight to board
        if len(input_val) == 0:
            lines = dev.read_lines()
            ph = lines[0]
            pH = ph.replace('\r', '')
        else:
            dev.send_cmd(input_val)
            time.sleep(1.3)
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