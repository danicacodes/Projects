#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Declare Dependancies
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
import pandas as pd
import requests


# In[2]:


# Choose executable path to driver (Windows User)
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# ### NASA Mars News

# In[3]:


# Visit NASA Mars News using splinter module
url = 'https://mars.nasa.gov/news'
browser.visit(url)


# In[4]:


# HTML Object
html = browser.html

# Use Beautiful Soup to parse HTML
soup = bs(html, 'html.parser')

# Collect the latest News Title and Paragraph Text. Assign the variables that you can reference later
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text

# Display Latest News Title & Paragraph Text
print(news_title)
print(news_p)


# ### JPL Mars Space Images - Featured Image

# In[5]:


# Visit the url for JPL Featured Space Image
url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url_image)


# In[6]:


#HTML Object
html_image = browser.html


# In[7]:


# Use Beautiful Soup to parse HTML
soup = bs(html_image, 'html.parser')


# In[8]:


# Retrieve image by assigning the url string to a variable called 'featured_image_url'
featured_image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');','')[1:-1]


# In[9]:


# Website URL
website_url = 'https://www.jpl.nasa.gov'


# In[10]:


# Merge Website URL with Scrapped route
featured_image_url = website_url + featured_image_url


# In[11]:


# Display complete url string for featured image on webpage
featured_image_url


# ### Mars Weather

# In[12]:


# Visit the Mars Weather Twitter Account
url_weather = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url_weather)


# In[13]:


# HTML Object
html_weather = browser.html


# In[14]:


# Use Beautiful Soup to parse HTML
soup = bs(html_weather, 'html.parser')


# In[15]:


# Find all elements that contain tweets
latest_tweets = soup.find_all('div', class_='js-tweet-text-container')


# In[16]:


#Looks at all tweets to find tweet with "sol"

for i in range(10):
    tweets = latest_tweets[i].text
    if "sol " in tweets:
        print(tweets)
        break


# ### Mars Facts

# In[17]:


# Visit url for Mars Facts
url_facts = pd.read_html('https://space-facts.com/mars/')
print(url_facts)


# In[18]:


# Mars Data Only 
mars_df = url_facts[1]
mars_df


# In[19]:


# Adds Columns to Data Frame
mars_df = url_facts[1]
mars_df.columns=['Description', 'Value']
mars_df


# ### Mars Hemispheres

# In[20]:


# Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres)


# In[21]:


# HTML Object
html_hemisphere = browser.html


# In[22]:


# Use Beautiful Soup to parse HTML
soup = bs(html_hemisphere, 'html.parser')


# In[23]:


# Find all elements with a class of item
items = soup.find_all('div', class_='item')


# In[24]:


#Define empty list
hemisphere_images = []


# In[25]:


# Main URL used to append images URL
hemisphere_url = 'https://astrogeology.usgs.gov'


# In[26]:


# Loop through the items
for i in items: 
    # Find & store title
    title = i.find('h3').text
    
    # Stores link to full image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    # Full image website 
    browser.visit(hemisphere_url + partial_img_url)
    
    # HTML Object 
    partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup 
    soup = bs( partial_img_html, 'html.parser')
    
    # Full image source 
    img_url = hemisphere_url + soup.find('img', class_='wide-image')['src']
    
    # Append to a list of dictionaries 
    hemisphere_images.append({"title" : title, "img_url" : img_url})
    
hemisphere_images


# In[28]:


get_ipython().system('jupyter nbconvert --to script mission_to_mars1.ipynb')

