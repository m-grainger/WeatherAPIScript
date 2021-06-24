# importing libraries
from datetime import datetime as dt
from pprint import pprint
import requests
import json
import time

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City ID for Portland, OR (from the tar.gz file on openweathermap.org)
CITY_ID = "5746545"

# Your API key
API_KEY = "<api key here>"

# updating the URL
URL = BASE_URL + "id=" + CITY_ID + "&appid=" + API_KEY

print(URL)
# Sending HTTP request
response = requests.get(URL)
print(response.status_code)

with open("weather_data.csv","a") as f:
    f.write("Time,Temp,FeelsLike,Humidity,Wind\n")

def k_to_f(k_temp):
    f_temp = round((int(k_temp) - 273.15) * 9/5 + 32, 2)
    return f_temp

def api_payload(api_data):
    # get current time
    now = dt.now()
    current_time = now.strftime("%H:%M:%S")
    # take the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']
    # getting feel like
    temp_feels_like = main['feels_like']  
    # getting the humidity
    humidity = main['humidity']
    # wind report
    wind_report = data['wind']['speed']
    
    temp_int = k_to_f(temperature)
    feels_int = k_to_f(temp_feels_like)
    
    # append to csv file
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
