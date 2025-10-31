#Task 1
import json
import requests

request = "https://api.chucknorris.io/jokes/random" 

try:
   response = requests.get(request)
   if response.status_code==200:
        response = response.json()
        print(f"Joke: {response['value']}")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")
   