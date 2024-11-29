import requests 
from rich import print 


def display_current_weather(city): 
  """Displays the current weather"""
  api_key = "0487517ao9045tca47fb9963d1b4be37"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

  response = requests.get(api_url)
  current_weather_data = response.json()
  current_weather_city = current_weather_data['city']
  current_weather_temperature =       current_weather_data['temperature']['current']
  
  print(f"The temperature in {current_weather_city} is {round(current_weather_temperature)}°C")

city_name = input("Enter a city: ")
city_name = city_name.strip()

if city_name: 
  display_current_weather(city_name)
else: 
  print("Please try again with a city")