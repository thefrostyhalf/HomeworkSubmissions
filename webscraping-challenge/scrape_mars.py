
# coding: utf-8

# In[49]:


from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from splinter import Browser
import time
import json
import tweepy
import apikeys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os


# In[50]:


url = 'https://mars.nasa.gov/news/'
path = '/Users/jackiemcguire/Desktop/portfolio/10-10-2017-UCB-Class-Repository-DATA/Homework/webscraping-challenge/chromedriver'
browser = webdriver.Chrome(path) 
# Retrieve page with the 'get' function from the browser object.  Then using
# 'page_source function to get html text

browser.get(url)
html = browser.page_source

# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(html, 'html.parser')
browser.close()


# In[51]:


soup_li = soup.find_all('li', class_='slide')


# In[52]:


titleslist = []
pgphlist = []

for article in soup_li:
    title = article.find('div', class_='content_title').text
    paragraph = article.find('div', class_='article_teaser_body').text
    titleslist.append(title)
    pgphlist.append(paragraph)


# In[53]:


splint_browser = Browser('chrome', executable_path=path,
                  headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
splint_browser.visit(url)
splint_browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(2)
splint_browser.click_link_by_partial_text('more info')


# In[54]:


html = splint_browser.html
soup = bs(html, 'html.parser')
splint_browser.quit()


# In[55]:


image_src = soup.find_all('figure', class_='lede')


# In[56]:


for each in image_src:
    print(each.a['href'])
    featured_image_url = 'https://www.jpl.nasa.gov'+each.a['href']


# In[57]:


consumer_key = apikeys.TWITTER_CONSUMER_KEY
consumer_secret = apikeys.TWITTER_CONSUMER_SECRET
access_token = apikeys.TWITTER_ACCESS_TOKEN
access_token_secret = apikeys.TWITTER_ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

public_tweets = api.user_timeline('marswxreport', count = 3)
for tweet in public_tweets:
    if (("hPa" in tweet['text']) and ("Sol" in tweet['text'])):
        mars_weather = tweet['text']
        break
        
print(mars_weather)


# In[58]:


url_tables = 'https://space-facts.com/mars/'

tables = pd.read_html(url_tables)

for each in tables:
    print(each)
    print("Tablelength: " + str(len(tables)))
    table_df = pd.DataFrame(tables[0])


# In[59]:


table_df = table_df.rename(columns={0:"planet_profile", 1:"mars_data"})
table_df = table_df.set_index('planet_profile')
table_df.head()


# In[60]:


table_html = pd.DataFrame.to_html(table_df)
hemispheres = pd.DataFrame(columns=['title', 'img_url'])


# In[61]:


splint_browser = Browser('chrome', executable_path=path,
                  headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
splint_browser.visit(url)

hemisphere_list = []

html = splint_browser.html
soup = bs(html, 'html.parser')
findHemisphere = soup.find_all('div', class_='item')

for each in findHemisphere:
    print(each.h3.text)
    hemisphere_list.append(each.h3.text)
    
splint_browser.quit()


# In[63]:


hemisphere_image = []

for eachHemi in hemisphere_list:

    splint_browser = Browser('chrome', executable_path=path,
                  headless=False)
    splint_browser.visit(url)
    time.sleep(2)
    splint_browser.click_link_by_partial_text(eachHemi)

    time.sleep(2)
    splint_browser.click_link_by_text('Sample')
    #Line 23
    splint_browser.windows.current = splint_browser.windows[1]
    #Line 24
    html = splint_browser.html
    soup = bs(html, 'html.parser')
    splint_browser.quit()
    #Line 25
    hemi_image = soup.body.find('img')['src']
    
    hemisphere_image.append(hemi_image)


# In[66]:


title_image_url = []
title_image_tuple = zip(hemisphere_list, hemisphere_image)
for each in title_image_tuple:
    temp_dict = {}
    temp_dict['title'] = each[0]
    temp_dict['img_url'] = each[1]
    title_image_url.append(temp_dict)
mars_dict = {'News Title': title, 'News Paragraph': paragraph, 'Featured Image':
    featured_image_url, 'Mars Weather': mars_weather, 'Mars Info': table_html,
    'Hemisphere Images': title_image_url}

