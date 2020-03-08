#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pymongo


# In[ ]:


executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# ## NASA Mars News

# In[ ]:


url = "https://mars.nasa.gov/news/"


# In[ ]:


response = requests.get(url)


# In[ ]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


print(soup.prettify())


# In[ ]:


results = soup.find("div", class_="features").text
print(results)


# In[ ]:


news_title = soup.find("div", class_="content_title").text
news_title = news_title.strip()    


# In[ ]:


news_p = soup.find("div", class_="image_and_description_container").text
news_p = news_p.strip()


# In[ ]:


print(f'Article Title:\n{news_title}.')
print('------------------------')
print(f'Paragraph:\n{news_p}')


# In[ ]:


browser.quit()


# In[ ]:


#Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pymongo


# In[ ]:


executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[ ]:


featured_img_pg_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(featured_img_pg_url)


# In[ ]:


slice_object = slice(24)
featured_img_pg_url = featured_img_pg_url[0:24]
featured_img_pg_url


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# In[ ]:


target_url = soup.find('footer')
link_portion = target_url.a['data-fancybox-href']
link_portion


# ### Featured Image URL

# In[ ]:


featured_image_url = (featured_img_pg_url.strip()) + link_portion
print(f'The URL string for the featured image is {featured_image_url}.')


# In[ ]:


browser.quit()


# In[ ]:


executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[ ]:


twitter_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(twitter_url)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# In[ ]:


first_tweet = soup.find("div", class_="js-tweet-text-container").text
mars_weather = first_tweet
mars_weather


# In[ ]:


browser.quit()


# In[ ]:


import pandas as pd

executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[ ]:


facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)


# In[ ]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# ### Mars Fact Table

# In[ ]:


fact_table = pd.read_html(facts_url)
fact_table_df = fact_table[0]
fact_table_df


# In[ ]:


table_html = fact_table_df.to_html()
print(table_html)


# In[ ]:


browser.quit()


# ## Mars Hemispheres

# In[ ]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pymongo


# In[ ]:


executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[ ]:


USGS_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
html = browser.html
browser.visit(USGS_url)
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())


# In[ ]:


html = browser.html
cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
browser.visit(cerberus_url)
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# In[ ]:


url_list = soup.find_all('div', class_="item")
print(url_list)


# In[ ]:


root_url = "https://astrogeology.usgs.gov"
img_urls = []

for url in url_list:
    title = url.find('h3').text
    img_search_url = url.find('a', class_="itemLink product-item")['href']   
    browser.visit(root_url + img_search_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
#     print(soup.prettify())
    
    img_url = root_url + soup.find('img', class_="wide-image")["src"]
#     print(img_url)
    
    img_urls.append({"Title" : title, "Image_URL" : img_url})
img_urls


# In[ ]:


print("Hemisphere Image URLs")
print("---------------------")
print(f'{img_urls[0]}')
print()
print(f'{img_urls[1]}')
print()      
print(f'{img_urls[2]}')
print()
print(f'{img_urls[3]}')     


# In[ ]:


browser.quit()

