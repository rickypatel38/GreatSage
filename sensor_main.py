import time
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

ec = check_ec()
ph = check_ph()
hum = check_humidity()
ltemp = check_liquid_temperature()
getrequests.update_thing_speak(ph, ec, ltemp, hum)

target_pH = 6.5

# Read pH value from sensor
pH = check_ph()

# Loop until target pH is reached
while pH < target_pH:
    flag = False
    # Start pump
    getrequests.start_pump()
    # Read pH value from sensor
    ph = check_ph()
    if abs(ph_value - pH) > 0.1:
        getrequests.update_thing_speak_ph(ph_value)
        pH = ph_value
    # Wait 1 minute
    time.sleep(180)

# Stop pump
getrequests.stop_pump()
