
# Dependencies
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
import sys 
import os 
import apikeys
import citipy
import random

# Save config information
url = "http://api.openweathermap.org/data/2.5/weather"

params = {'appid': apikeys.weather_api,
          'q': '',
          'units': 'metric'}

weather_data = []
coords=[]
cities = []

# Loop through the list of cities and perform a request for data on each
for i in range(500):
	cities.append((citipy.nearest_city(str(random.randint(-9000,9000)/100)+", "+(str(random.randint(-18000,18000)/100))).city_name)
print([cities])