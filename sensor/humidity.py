import serial
import sys
import time
import string 
import os
from serial import SerialException


# Find the symbolic link for the USB serial device with the desired name in the /dev/serial/by-id directory
serial_by_id_path = os.path.join("/dev", "serial", "by-id")
for filename in os.listdir(serial_by_id_path):
    if filename == "usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0":
        serial_path = os.path.join(serial_by_id_path, filename)
        break

 

def read_line(ser):
    """
    Read a line from the serial device, ending in a line separator "\r".
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
    Read multiple lines from the serial device, using the modified read_line function.
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
    Send command to the device.
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
            
def read_humidity():
    try:
        ser = serial.Serial(serial_path, 9600, timeout=0)
    except serial.SerialException as e:
        print( "Error, ", e)
        sys.exit(0)

    input_val = "R"
    send_cmd(input_val, ser)
    time.sleep(1.3)
    lines = read_lines(ser)
    for i in range(len(lines)):
        val = lines[i].decode('utf-8')
    print("Humidity:", val) 
    return val
