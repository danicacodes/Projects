#!/usr/bin/env python
# coding: utf-8



# Declare Dependancies
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
import pandas as pd
import requests



#initialize browser
def scrape():
        # Choose executable path to driver (Windows User)
        #executable_path = {"executable_path": "chromedriver.exe"}
        #browser = Browser("chrome", **executable_path, headless=False)
        browser = Browser("chrome", executable_path = 'chromedriver.exe', headless=False)
        news_title, news_p = scrape_mars_news(browser)
        #featured_image_url = scrape_mars_image(browser)

        mars_info = {'news_title': news_title, 
        'news_p': news_p, 
        'featured_image_url': scrape_mars_image(browser),
        'weather_tweet': scrape_mars_weather(browser),
        'data': scrape_mars_facts(),
        }

        browser.quit()
        
        return mars_info

# ### NASA Mars News

# NASA MARS NEWS



def scrape_mars_news(browser):
        # try:
        #browser = init_browser()
        url = 'https://mars.nasa.gov/news'      
        browser.visit(url)


        html = browser.html
        # Use Beautiful Soup to parse HTML
        soup = bs(html, 'html.parser')
        
        # Collect the latest News Title and Paragraph Text. Assign the variables that you can reference later
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text
        
        # Dictionaries
        #mars_info['news_title'] = news_title
        #mars_info['news_paragraph'] = news_p

        return news_title, news_p

        # finally:
        #         browser.quit()


# ### JPL Mars Space Images - Featured Image

def scrape_mars_image(browser):
        # try:
        # Initialize Browser
        #browser = init_browser()

        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featured_image_url)

        html_image = browser.html
        soup = bs(html_image, 'html.parser')

        featured_image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        website_url = 'https://www.jpl.nasa.gov'


        # Merge Website URL with Scrapped route
        featured_image_url = website_url + featured_image_url

        # Display complete url string for featured image on webpage
        featured_image_url

        # mars_info['featured_image_url'] = featured_image_url

        return featured_image_url

        # finally: 
        #         browser.quit()

### Mars Weather

def scrape_mars_weather(browser):
        # try:
        # # Initialize Browser
        #browser = init_browser()

        # Visit the Mars Weather Twitter Account
        url_weather = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(url_weather)

        # HTML Object
        html_weather = browser.html

        # Use Beautiful Soup to parse HTML
        soup = bs(html_weather, 'html.parser')

        # Find all elements that contain tweets
        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

        #Looks at all tweets to find tweet with "sol"

        #for i in range(10):
        for tweets in latest_tweets:
                weather_tweet = tweets.find('p').text
                if 'sol' in weather_tweet:
                        print(weather_tweet)
                        break
                else:
                        pass
        #tweets = latest_tweets[i].text
        #if "sol " in tweets:
        #print(tweets)
        #break

        # mars_info['weather_tweet'] = weather_tweet
        return weather_tweet
        # finally:
        #         browser.quit()

#### Mars Facts

def scrape_mars_facts():
        # Visit url for Mars Facts
        # Not really scrapping, just reading a table
        url_facts = 'https://space-facts.com/mars/'
        mars_facts = pd.read_html(url_facts)


        # Mars Data Only 
        mars_df = mars_facts[1]

        # Adds Columns to Data Frame
        #mars_df = url_facts[1]
        mars_df.columns = ['Description', 'Value']
        #mars_df

        mars_df.set_index('Description', inplace=True)

        data = mars_df.to_html()

        # mars_info['mars_facts'] = data

        return data

# ### Mars Hemispheres

def scrape_mars_hemispheres(browser):
        #try:
        #  # Initialize Browser
        #browser = init_browser()


                # Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
        hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres)



        # HTML Object
        html_hemisphere = browser.html



        # Use Beautiful Soup to parse HTML
        soup = bs(html_hemisphere, 'html.parser')



        # Find all elements with a class of item
        items = soup.find_all('div', class_='item')



        #Define empty list
        hemisphere_images = []



        # Main URL used to append images URL
        hemisphere_url = 'https://astrogeology.usgs.gov'



        # Loop through the items
        for i in items: 
                # Find & store title
                title = i.find('h3').text

                # Stores link to full image website
                partial_img_url = i.find('a', class_='itemLink product-item')['href']

                # Full image website 
                browser.visit(hemisphere_url + partial_img_url)

                #  HTML Object 
                partial_img_html = browser.html

                # Parse HTML with Beautiful Soup 
                soup = bs( partial_img_html, 'html.parser')

                # Full image source 
                img_url = hemisphere_url + soup.find('img', class_='wide-image')['src']

                # Append to a list of dictionaries 
                hemisphere_images.append({"title" : title, "img_url" : img_url})

        # mars_info['hemisphere_images'] = hemisphere_images

        return hemisphere_images
# finally:
#         browser.quit()

if __name__ == "__main__":

        print(scrape())