import pandas as pd
from splinter import Browser
from time import sleep
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import pymongo
import time

news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
jpl_base = 'https://www.jpl.nasa.gov'
hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
facts_url = 'https://space-facts.com/mars/'



def init_browser():

    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
    
def scrape():
    mars_data = {}
    browser = init_browser()
    browser.visit(news_url)
    html = browser.html
    news_data = BeautifulSoup(html, "html.parser")
    #strip headline
    news_headline = news_data.find_all('div', class_='content_title')[1].text.strip()
    #strip body
    news_desc = news_data.find_all('div', class_='article_teaser_body')[0].text.strip()
    
    mars_data.update( {
        'news_headline': news_headline,
        'news_description': news_desc
    })

    # JPL Featureed Space Image
    sleep(1)
    browser.visit(jpl_url)
    html = browser.html
    JPL_image = BeautifulSoup(html, "html.parser")

    featured_image = JPL_image.find(class_='carousel_item')['style']
    image_urlend = featured_image.split("'")[1]
    image_url = jpl_base + image_urlend
    mars_data.update( {
        "featured_img": image_url
    })

    # Mars Facts tabels
    sleep(1)
    Facts_Tabels = pd.read_html(facts_url)
    tabels_df = Facts_Tabels[0]
    tabels_df.columns = ['Item', 'Values']
    tabels_df.set_index('Item', inplace=True)
    html_table = tabels_df.to_html(
        classes='table table-striped table-hover')

    mars_data.update({
        "html tabel": html_table
    })

    browser.visit(hemi_url)

    # Hemisphere images

    sleep(1)
    html = browser.html
    hemi_image = BeautifulSoup(html, "html.parser")
    hemi_urls = hemi_image.find_all('div', class_='item')
    hemi_photos_urls = []

    for x in hemi_urls:
        title = x.find('h3').text
        url = x.find('img', class_='thumb')['src']
        hemi_photos_urls.append(
            {'title': title, 'url': 'https://astrogeology.usgs.gov' + url})

    mars_data.update({
        "hemishere urls": hemi_photos_urls
        })
    
    browser.quit()

    print(mars_data)

    return mars_data




