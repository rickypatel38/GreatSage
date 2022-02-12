# README #

### What Is GreatSage?  
The purpose of GreatSage is to provide an automated greenhouse monitoring system. The sensors in this project are utilized in order to provide insight into the conditions of the plant growing environment. Outside weather conditions data is retrieved from the NOAA API service. Overtime a correaltion between environmental conditions within the greenhouse and the weather outside can be made. This correlation should in theory provide a "predictive analytics" for the user to be able to predict conditions inside the greenhouse based on future forecast. It should also provide insight into the amount of energy expenditure that may occur, based on the upcoming weather, in order to maintain ideal growing conditions within the greenhouse.
The sensors in this system should provide enough data in order to calculate information such as the Vapor Pressure Deficit (VPD) in the growing environment. The sensors will also provide insight in to the pH, EC, and liquid temperature of the grow solution. The power for this equipment will be controlled via a "web-power switch" so that the user can control the greenhouse equipment remotely at any given time. 

### Future Updates  
Future goals for this project includes developing a system which will control the water pumps, chemical injections into the water, and the lighting systems based on PAR (Photo-Active Radition) measurements. A CO2 sensor will also be added to this project in order to monitor CO2 levels in the greenhouse for plant photosynthesis and should allow for stomal opening calculations to occur. 

### Data Points  
* EC (Electric Conductivity)   
* Ambient Humidity
* Ambient Temperature
* Liquid Temperature 
* pH

* Adding OpenWeather API funcitonality in order to have redunancy for when NOAA API is down. 
        * Weather Conditions Description
        * Feels Like
        * Humidity
        * Pressure
        * Temperature
        * Temperature Max
        * Temperature Min
        * Wind Direction (Degrees)
        * Wind Speed
        * Cloud Coverage
        * Datetime

* Local weather conditions utilizing NOAA SDK: (National Ocean and Atmospheric Administration)
    * temperature         
    * dewpoint        
    * windDirection   
    * windSpeed       
    * windGust        
    * barometricPressure 
    * seaLevelPressure   
    * visibility         
    * max temp in past 24hrs          
    * min temp in past 24hrs                  
    * relativeHumidity   
    * windChill          
    * heatIndex          
    * cloudLayer

### Hardware / Sensors ###
Read up on how the sensors work from the links below. Both pH and EC sensors are converted from EZO pins to USB data there is a github link on the atlas scientific website. 

* pH:                                        https://www.atlas-scientific.com/product_pages/probes/ph_probe.html
* electric conductivity:                     https://www.atlas-scientific.com/product_pages/kits/ec_k1_0_kit.html 
* Board for pH & EC for plug and play USB    https://www.atlas-scientific.com/product_pages/components/usb-iso.html
* DS18B20 waterproof temperature sensor:     https://www.dfrobot.com/product-689.html 
* DHT22 humidity + temperature sensor:       https://www.adafruit.com/product/385 
* DS18B20 temperature sensor wiring:         https://learn.adafruit.com/using-ds18b20-temperature-sensor-with-circuitpython/hardware
* DHT22 wiring:                              https://www.instructables.com/id/Raspberry-Pi-Tutorial-How-to-Use-the-DHT-22/
* Web Power Switch for controlling power:    https://www.digital-loggers.com/lpc.html 
* Web Power Switch Code:                     https://github.com/dwighthubbard/python-dlipower/blob/master/dlipower/dlipower.py
* Web Power Switch Python Import:            https://pypi.org/project/dlipower/

* DHT22 code: sensor --> ht_sensor.py        sensor_gpio = 23 #GPIO Pin location on Raspberry Pi
* pH Sensor code: sensor --> ph_sensor.py    line 14 "index = 1" assumption is made that the sensor is plugged into the index location of USB 1. 
* EC Sensor code: sensor --> ec_sensor.py    line 28 "index = 0" assumption is made that the sensor is plugged into the index  location of USB 0. 

### Architecture ###
* Python v3.7
* SQlite3 is the Database.
* Fast API is the API Service
* Pipenv is the virtual development environmnet. (No need to install dependencies for this project on your OS when you can install a virtual env.)
* DB SQLite3:                               https://www.sqlite.org/index.html
* Fast API:                                 https://github.com/tiangolo/fastapi
* Pipenv:                                   https://github.com/pypa/pipenv 
* NOAA SDK:                                 https://github.com/paulokuong/noaa 

### How do I get set up? ###

* Dependencies: The init.sh script will install all of the required dependencies for this project. 
* Pipenv: Run the Pipenv Install then Pipenv Update commands. From there all dependencies should be installed to run this project. 
* Database configuration: Run the db_init.py file within the "sqlite" folder. This will create your sqlite database with the approriate tables. 
* Deployment instructions: Once all the sensors have been wired run the sensor_main.py file in order to store data from the sensors in to the SQLite DB as a test to see if the sensors are properly connected. 
* A .env file with the variables below is required: 
    * DB_PATH = 'your\path\to\greatsage.db'
    * LOG_PATH = 'your\path\to\logs'
    * API_KEY = your openweather API Key 
* Run the api_main.py file in order to run the API Service on 0.0.0.0 (your local area network).  
* All datetime data is stored in UTC.

### Security ### 
* ToDo: Input validation on all API Endpoints (regex reccomended).
* ToDo: More defensive coding for the Web Power Switch
* ToDo: API Token based authentication.
* Line 20 in api_main.py as * for CORS please replace the wildcard value with the address of the frontend endpoint which will utilize the API. 
* Unforutnately the temperature sensor requires admin access to read sys/bus/w1/devices/w1_slave. This will need to be re-written. A seperate service running on the OS should call the temperature sensor and store it into the DB.  
* It is bad practice to run the API service on a production environment as admin. 

### Code Cleanup ###
* ToDo: More robust error logging on indidivual sensors. 
    * pH Sensor Error Catching / Logging
    * EC Sensor Error Catching / Logging
    * DS18B20 Sensor Error Catching / Logging
    * DHT22 Sensor Error Catching / Logging 
    * WebPowerSwitch Error Catching / Logging 
    * Create a "isDown" table to have status of each sensor. 
    * Create an alerting system that alerts if the Raspberry Pi itself is down. 

### Features ### 
* Log when Powerswitch is turned off and on in DB. 
* Add a "tags" for the powerswitch number i.e. Switch 1 is "Main Lights"


### Contribution guidelines ###
* To be created / performed: 
* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin:  Ricky A. Patel
* Email:                RP2992@outlook.com 
* Linkedin:             https://www.linkedin.com/in/rickypatel38/ 