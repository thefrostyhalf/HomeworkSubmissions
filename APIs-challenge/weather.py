
# coding: utf-8

# # Python APIs
# ## Jackie McGuire
# 
# This code uses the Open Weather Map API to retrieve a user-defined number of cities and create scatterplots for Temperature, Humidity, Cloudiness and Windiness. 
# 
# Note: There is a 1-second wait built-in wile looping between cities to avoid going over the 60-city per minute of the free OMW account API Key. 

# In[2]:


# Set dependencies
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
import sys 
import os 
import apikeys
from citipy import citipy
import random
import time
import datetime


# In[ ]:


# Set API call information
url = "http://api.openweathermap.org/data/2.5/weather"

params = {'appid': apikeys.OMW_API_KEY,
          'q': '',
          'units': 'metric'}
# Set empty list for Weather Data
weather_data = []
# Set empty set for cities (to prevent repeat-data)
cities = set() # Using set prevents duplicates
# User input for number of cities
dataset_number = input("How many random cities (@60 cities per minute) would you like to get data for?")
# Give user estimate of time to complete request
print("Fetching "+dataset_number+" records. This will take approximately "+str(int(dataset_number)//60)+" minutes and "+str(int(dataset_number)%60)+" seconds.")


# In[29]:



apireq = 1 #This counts API requests 
idx=1 #This counts cities successfully added (excluding 'city not found')
#using while len(weather_data) here helps to make sure we get the full number of cities, accounting for 404 errors.
while len(weather_data)<int(dataset_number):
    oldcitieslen = len(cities)
    newcitieslen = len(cities)
    while newcitieslen==oldcitieslen:
        city = citipy.nearest_city((random.randint(-9000,9000)/100),(random.randint(-18000,18000)/100))
        city_name = city.city_name
        country_code = city.country_code
        newcity=(city_name+","+country_code.upper())
        cities.add(newcity)
        newcitieslen = len(cities)
    params['q'] = newcity
    response=req.get(url, params=params)
    response_json = response.json()
    if response_json["cod"]==200:
        weather_data.append(response.json())
        print("API Request ",apireq, ", City Number", idx , ", Weather Data For ", newcity,"\n", response.url, "...Successful")
        apireq=apireq+1
        idx=idx+1
        time.sleep(1)   
    else:
        print("API Request ", apireq , " Weather Data For ", newcity,"\n", response.url, "...ERROR:", response_json["cod"], response_json["message"],"CITY NOT ADDED TO DATA")
        apireq=apireq+1
        time.sleep(1)


# In[37]:


# Print successrate of API calls
print ("API Request completed. Error rate was "+str(1-(idx/apireq))+"%. "+str(apireq-1)+" cities fetched, "+str(idx-1)+" cities found.")


# In[38]:


# Set empty lists for API data
name_data=[]
lat_data = []
temp_data = []
humid_data=[]
cloud_data=[]
wind_data=[]
# Create dictionary with lists
weather_dict = {"City Name": name_data,
                            "Temperature": temp_data, 
                            "Latitude": lat_data, 
                           "Humidity":humid_data,
                           "Cloudiness": cloud_data,
                           "Windiness": wind_data}


# In[39]:


# Add Weather data to table
for data in weather_data:
        name_data.append(data["name"])
        lat_data.append(data['coord']['lat'])
        temp_data.append(data['main']['temp'])
        humid_data.append(data['main']['humidity'])
        cloud_data.append(data["clouds"]["all"])
        wind_data.append(data["wind"]["speed"])


# In[40]:


# Create DataFrame from table
weather_data_df = pd.DataFrame(weather_dict)
# Save DataFrame to csv
weather_data_df.to_csv("weatherdata.csv")


# In[41]:


# Set variable for printing current date on charts
now = datetime.datetime.now()
# Define function for creating latitude-based charts with diffrent variables
def latitude_graph(variable):
    fig, ax = plt.subplots()
    weather_data_df.plot(kind="scatter", x="Latitude", y=variable, s=50, c=variable, cmap="seismic", ax=ax)
    ax.set_title(variable+" by Latitude "+(now.strftime("%Y-%m-%d %H:%M")))
    ax.set_xlabel("Latitude of Cities")
    ax.set_ylabel("Current "+variable)
    plt.grid()
    plt.savefig(variable+"ByLatitude")
    plt.show()
# Temperature graph
temp_lat_graph = latitude_graph("Temperature")


# In[42]:


# Humidity Graph
humid_lat_graph =latitude_graph("Humidity")


# In[43]:


# Cloud Graph
cloud_lat_graph = latitude_graph("Cloudiness")


# In[44]:


# Wind Graph
wind_lat_graph = latitude_graph("Windiness")

