import time
import logging
import pylibftdi
import datetime
from .atlas import AtlasDevice 
from .atlas import get_ftdi_device_list

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)
date = str(datetime.datetime.utcnow())
device_list = None

def read_tank_ec():
    devices = list(get_ftdi_device_list())
    input_val = 'R'
    dev = None
    for index in range(len(devices)):
        try:
            dev = AtlasDevice(devices[int(index)])
            break
        except (pylibftdi.FtdiError, Exception) as e:
            logging.error("Failure: {}, Date:{}".format(e, date))
    if dev:
        dev.flush()
        try:
            dev.send_cmd(input_val)
            time.sleep(0.5)
            lines = dev.read_lines()
            ec = lines[0].replace('\r', '')
        except Exception as e:
            logging.error("EC failure line 39, Error:{}, Date:{}".format(e, date))
        if ec is not None:
            print("EC:", ec)
            logging.debug("EC:{}, DateTime:{}".format(ec, date))
            return ec
        else:
            logging.error("EC Failure Line 44: {}".format(date))
    else:
        print("Device Not Found")

