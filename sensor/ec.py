import time
import logging
import pylibftdi
import datetime
from .atlas import AtlasDevice 
from .atlas import get_ftdi_device_list

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)
date = str(datetime.datetime.utcnow())


def read_tank_ec():
    device_list = get_ftdi_device_list()
    if device_list is None:
        device_list = get_ftdi_device_list()
    while True:
        index = 0
        try:
            dev = AtlasDevice(device_list[int(index)])
            break
        except pylibftdi.FtdiError as e:
            logging.error("Failure: {}, Date:{}".format(e, date))
    dev.flush()
    try:
        input_val = 'R'
        # pass commands straight to board
        if len(input_val) == 0:
            lines = dev.read_lines()
            EC = lines[0]
            ec = EC.replace('\r', '')
        else:
            dev.send_cmd(input_val)
            time.sleep(1.3)
            lines = dev.read_lines()
            EC = lines[0]
            ec = EC.replace('\r', '')
    except:
        logging.error("EC failure line 39, Date:{}".format(date))

    if ec is not None:
        print("EC:", ec)
        logging.debug("EC:{}, DateTime:{}".format(ec, date))
        return ec
    else:
        logging.error("EC Failure Line 44: {}".format(date))