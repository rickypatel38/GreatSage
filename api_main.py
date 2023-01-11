#!/usr/bin/env python3
from api import getrequests
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sensor_main
import os
import uvicorn
import json

load_dotenv() #Load variables from .env file to environment
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # SECURITY -- It is bad practice to allow * please change this to the approriate front-end endpoint only!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log_path = os.getenv("LOG_PATH") #pull the log path from .env file

@app.get("/read_sensors")
def read_sensors():
    return sensor_main.read_all_sensors()

@app.get("/switch_off/{outlet}")
def outlet_off(outlet: int):
    return getrequests.switch_off(outlet)

@app.get("/switch_on/{outlet}")
def outlet_on(outlet: int):
    return getrequests.switch_on(outlet)

@app.get("/switch_status")
def outlet_status():
    return getrequests.switch_status
     

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
    #Running on 0.0.0.0 instead of 127.0.0.1 allows it to be accessible on LAN rather than just on local machine only.