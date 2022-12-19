import requests
import json

# Read coordinates from JSON file
with open('coordinates.json') as json_file:
    coordinates = json.load(json_file)

# Construct the API request
url = 'http://api.weatherapi.com/v1/current.json?'
api_key = ''
lat = coordinates['latitude']
lon = coordinates['longitude']
params = {'key': api_key, 'q': f'{lat},{lon}'}

# Make the request
response = requests.get(url, params=params)

# Read and parse the response
data = response.json()

# Print the weather data
print(f'The temperature is {data["current"]["temp_c"]}°C and the weather is {data["current"]["condition"]["text"]}.') 
