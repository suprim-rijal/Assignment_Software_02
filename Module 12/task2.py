
#Task 2
#I have remove my API key form this program, because GIThub consider it as a threat.
import json
import requests

municipality = input("Enter the municipality/city name:").capitalize()
myAPI_key = input("Enter your API key:")

request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={myAPI_key}" 

try:
   
   response = requests.get(request)
   if response.status_code==200:
        response = response.json()
        weather = response['weather'][0]['main']
        weather_description = response['weather'][0]['description']
        temperature = response['main']['temp']
        print(f"Weather condition in {municipality}: {weather}. More descriptively, {municipality} has {weather_description}.")
        print(f"The temperature in {municipality} is about {(temperature-273.15):.2f}° Celcius.")
   else:
       print("Something wrong with the entered Municipality name!!!")

            
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")




    

