# importing modules
from datetime import datetime as dt
from pprint import pprint
import requests
import json
import time

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = "Munich"

# Your API key
API_KEY = "<enter key here>"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

print(URL)
# Sending HTTP request
response = requests.get(URL)
print(response.status_code)

with open("weather_data.csv","a") as f:
    f.write("Time,Temp,FeelsLike,Humidity,Wind\n")

def api_payload(api_data):
    # get current time
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    # take the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']
    # getting feel like
    temp_feel_like = main['feels_like']  
    # getting the humidity
    humidity = main['humidity']
    # wind report
    wind_report = data['wind']['speed']
    
    '''
    print(f"Temperature: {temperature}")
    print(f"Feel Like: {temp_feel_like}")    
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind_report['speed']}")
    print(f"Time Zone: {data['timezone']}")
    '''
    
    temp_int = int(temperature)
    feels_int = int(temp_feel_like)
    farenheit_temp = (temp_int - 273.15) * 9/5 + 32 
    farenheit_feels_like = (feels_int - 273.15) * 9/5 + 32 
    temp_int = round(farenheit_temp,2)
    feels_int = round(farenheit_feels_like,2)

    with open("weather_data.csv","a") as f:
        f.write(f'{current_time},{temp_int},{feels_int},{humidity},{wind_report}\n')

if response.status_code == 200:
    try: 
        # retrieving data in the json format
        data = response.json()
        # pprint(data)    
    except Exception as e:
        print(f"error: {e}")
else:
   # showing the error message
   print("Error in the HTTP request")
counter = 0
while True:
    counter += 1
    print(f"iteration: {counter}")
    api_payload(data)
    time.sleep(60)
