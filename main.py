import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

report=open('whether-report.txt','w')
report.write ("-------------------------------------------------------------\n")
report.write ("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
report.write ("-------------------------------------------------------------\n")

report.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
report.write("Current weather desc  :{}\n".format(weather_desc))
report.write("Current Humidity      :{} %\n".format(hmdt))
report.write("Current wind speed    :{} kmph\n".format(wind_spd))
report.close()