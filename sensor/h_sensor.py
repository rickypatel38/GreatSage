#!/usr/bin/python

import serial
import sys
import time
import string 
from serial import SerialException

usbport = '/dev/ttyUSB0' # change to match your pi's setup 

def read_line(ser):
    """
    taken from the ftdi library and modified to 
    use the ezo line separator "\r"
    """
    lsl = len(b'\r')
    line_buffer = []
    while True:
        next_char = ser.read(1)
        if next_char == b'':
            break
        line_buffer.append(next_char)
        if (len(line_buffer) >= lsl and
                line_buffer[-lsl:] == [b'\r']):
            break
    return b''.join(line_buffer)
    
def read_lines(ser):
    """
    also taken from ftdi lib to work with modified readline function
    """
    lines = []
    try:
        while True:
            line = read_line(ser)
            if not line:
                break
                ser.flush_input()
            lines.append(line)
        return lines
    
    except SerialException as e:
        print( "Error, ", e)
        return None	

def send_cmd(cmd, ser):
    """
    Send command to the Atlas Sensor.
    Before sending, add Carriage Return at the end of the command.
    :param cmd:
    :return:
    """
    buf = cmd + "\r"     	# add carriage return
    try:
        ser.write(buf.encode('utf-8'))
        return True
    except SerialException as e:
        print ("Error, ", e)
        return None
            
def get_humidity():

    try:
        ser = serial.Serial(usbport, 9600, timeout=0)
    except serial.SerialException as e:
        print( "Error, ", e)
        sys.exit(0)

    while True:
        input_val = "R"
        send_cmd(input_val, ser)
        time.sleep(1.3)
        lines = read_lines(ser)
        for i in range(len(lines)):
            #print( lines[i].decode('utf-8'))
            val = lines[i].decode('utf-8')
        return val
           