import time
import json
import os

loggingDirectory = os.path.abspath(os.path.join(os.getcwd(), 'logs'))

def writeToFile(filename, data):
    with open(os.path.join(loggingDirectory, filename), 'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def logTime():
    epoch_time = int(time.time())
    d = {"time":epoch_time,"comment":"Weather data last received."}
    with open(os.path.join(loggingDirectory, 'logs.json'), 'w+', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)

def checkLastLogTime():
     with open(os.path.join(loggingDirectory, 'logs.json')) as data_file:    
        data = json.load(data_file)
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['time']))