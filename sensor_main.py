import time
import math
from sensor import ec, temperature, ph, humidity
from api import getrequests

def check_ec():
    value = float(ec.read_tank_ec())
    return value

def check_ph():
    value = float(ph.read_tank_ph())
    return value

def check_liquid_temperature():
    value = float(temperature.read_temperature())
    return  value

def check_humidity():
    value = float(humidity.read_humidity())
    return value

def calculate_vpd(temp_c, humidity):
    #Using the Magnus formula
    # Saturation vapor pressure (kPa) at temperature temp_c
    temp = temp_c + 2.5
    e_s = 0.6108 * math.exp((17.27 * temp) / (temp + 237.3))
    # Actual vapor pressure (kPa)
    e_a = (humidity / 100) * e_s
    # Vapor pressure deficit (kPa)
    vpd = e_s - e_a
    print("VPD:", vpd)
    return vpd


def read_all_sensors():
    ec = check_ec()
    ph = check_ph()
    hum = check_humidity()
    ltemp = check_liquid_temperature()
    vpd = calculate_vpd(ltemp, hum)
    getrequests.update_thing_speak(ph, ec, ltemp, hum, vpd)

read_all_sensors()
#target_pH = 6.5

# Read pH value from sensor
#pH = check_ph()

# Loop until target pH is reached
#while pH < target_pH:
#    flag = False
    # Start pump
#    getrequests.start_pump()
    # Read pH value from sensor
#    ph = check_ph()
#    if abs(ph_value - pH) > 0.1:
#        getrequests.update_thing_speak_ph(ph_value)
#        pH = ph_value
    # Wait 1 minute
#    time.sleep(180)

# Stop pump
#getrequests.stop_pump()
