import serial
import sys
import time
import string 
import os
from serial import SerialException

def read_line(ser):
    """
    Read a line from the serial device, ending in a line separator "\r".
    """
    lsl = len(b'\r')
    line_buffer = bytearray()
    while True:
        next_char = ser.read(1)
        if next_char == b'' or next_char == b'\r':
            break
        line_buffer.append(next_char[0])
    return bytes(line_buffer)

def read_lines(ser):
    """
    Read multiple lines from the serial device, using the modified read_line function.
    """
    lines = []
    while True:
        line = read_line(ser).decode()
        if line:
            lines.append(line)
        else:
            break
    return lines

def send_cmd(cmd, ser):
    """
    Send command to the device.
    Before sending, add Carriage Return at the end of the command.
    """
    buf = cmd + "\r"
    ser.write(buf.encode())
    time.sleep(0.1)

def read_humidity():
    try:
        with serial.Serial('/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0', 9600, timeout=0) as ser:
            send_cmd('R', ser)
            time.sleep(0.5)
            humidity = read_lines(ser)[0]
            print("Humidity:", humidity) 
            return humidity
    except serial.SerialException as e:
        print(f"Error: {e}")
        return None
