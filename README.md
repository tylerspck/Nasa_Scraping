# Webscraping NASA Data + Web Application Building

## Object

Build a web application that scrapes various websites for Mars-related data (NASA.gov), and displays the scraped information in a single HTML page. 

## Scraping process using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter

[NASA Mars News Site](https://mars.nasa.gov/news/): 

* Scraped using BeautifulSoup. 

JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars):

* Used splinter to navigate the site, then find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

Mars Weather Twitter account [here](https://twitter.com/marswxreport?lang=en)

* Scraped the latest Mars weather tweet from the page and saved the tweet text for the weather report as a variable called `mars_weather`.

Mars Facts webpage [here](https://space-facts.com/mars/)

* Used Pandas to scrape the table from this website that contains facts about Mars (diameter, mass, etc.)
* Used Pandas to convert the data to an HTML table string.

USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 

* Found the image URL to the full resolution image for each of Mars' hemispheres.
* Used Python dictionary to store the data using the keys `img_url` and `title`.
* Appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

## Website Building Using MongoDB, Flask, Bootstrap

Created a new HTML page showing the information scraped from the aforementioned URLs. 

* Converted my Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` to execute and return one Python dictionary containing all of the scraped data.
* Created a route called `/scrape` to import the `scrape_mars.py` script and call the `scrape` function.
* Stored the return value in Mongo as a Python dictionary.
* Created a root route `/` that will query the Mongo database and pass the Mars data into an HTML template to display the data.
* Created a the HTML file `index.html` that will take the Mars data dictionary and display all of the data in the appropriate HTML elements. 
* Used Bootstrap to structure the HTML website.
