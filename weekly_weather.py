# importing modules
from datetime import datetime as dt
from pprint import pprint
import requests
import json
import time

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"

# lat and long for Portland, OR (from the tar.gz file on openweathermap.org)
LAT = 45.523449
LONG = -122.676208

# Your API key
API_KEY = "<api key here>"

# updating the URL
URL = f"{BASE_URL}lat={LAT}&lon={LONG}&appid={API_KEY}"

print(URL)
# Sending HTTP request
response = requests.get(URL)
print(response.status_code)

with open("historical_weather_data.csv","a") as f:
    f.write("Time,Temp,Type\n")

def k_to_f(k_temp):
    f_temp = round((int(k_temp) - 273.15) * 9/5 + 32, 2)
    return f_temp

def utc_to_human(utc):
    return dt.utcfromtimestamp(int(utc)).strftime('%m-%d')

if response.status_code == 200:
    try: 
        # retrieving data in the json format
        data = response.json()
        #pprint(data['daily'])    
        for days in data['daily']:
            time = utc_to_human(days['dt'])
            temp = k_to_f(days['temp']['day'])
            with open("historical_weather_data.csv", "a") as f:
                f.write(f"{time},{temp},Actual\n")
            feels = k_to_f(days['feels_like']['day'])
            with open("historical_weather_data.csv", "a") as f:
                f.write(f"{time},{feels},Feels Like\n")
    except Exception as e:
        print(f"error: {e}")
else:
   # showing the error message
   print("Error in the HTTP request")
