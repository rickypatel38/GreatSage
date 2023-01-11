from dotenv import load_dotenv
import dlipower
import requests
import json
import os

load_dotenv() #Load variables from .env file to environment
iot_key = os.getenv("THINGSPEAK_KEY")
switch_key = os.getenv("DLI_PASS")
powerSwitch = "192.168.0.100"

def update_thing_speak(ph, ec, temp, hum, vpd):
    url_string = "https://api.thingspeak.com/update?api_key="+iot_key+"&field1="+str(ph)+"&field2="+str(ec)+"&field3="+str(temp)+"&field4="+str(hum)+"&field5="+str(vpd)
    r = requests.get(url=url_string)
    data = r.json()
    return data

def update_thing_speak_ph(ph):
    url_string = "https://api.thingspeak.com/update?api_key="+iot_key+"&field1="+str(ph)
    r = requests.get(url=url_string)
    data = r.json()
    return data

def switch_off(num):
    print('Connecting to a DLI PowerSwitch at 192.168.1.140')
    switch = dlipower.PowerSwitch(hostname=powerSwitch, userid="admin", password=switch_key)
    print('Turning OFF the outlet')
    switch.off(num)
    status = switch[num-1].state
    switch.session.close()
    return('The current status of Outlet:'+str(num)+ ' is: '+status)

def switch_on(num):
    print('Connecting to a DLI PowerSwitch at 192.168.1.140')
    switch = dlipower.PowerSwitch(hostname=powerSwitch, userid="admin", password=switch_key)
    print('Turning ON the outlet')
    switch.on(num)
    status = switch[num-1].state
    switch.session.close()
    return('The current status of Outlet:'+str(num)+ ' is: '+status)

def switch_status(num):
    print('Connecting to a DLI PowerSwitch at 192.168.1.140')
    switch = dlipower.PowerSwitch(hostname=powerSwitch, userid="admin", password=switch_key)
    switchValues = switch
    switch.session.close()
    return('The current status of the powerswitch is:', switchValues)

def start_pump():
    requests.get("http://example.com/start_pump")

# Function to stop pump
def stop_pump():
    requests.get("http://example.com/stop_pump")