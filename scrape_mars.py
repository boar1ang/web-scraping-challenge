#!/usr/bin/env python
# coding: utf-8

#Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pandas as pd
import pymongo

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# ## NASA Mars News
def scrape_mars_news():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())
    results = soup.find("div", class_="features").text
    print(results)

    news_title = soup.find("div", class_="content_title").text
    news_title = news_title.strip()    

    news_p = soup.find("div", class_="image_and_description_container").text
    news_p = news_p.strip()

    print(f'Article Title:\n{news_title}.')
    print('------------------------')
    print(f'Paragraph:\n{news_p}')
    
    
    

    #executable_path = {"executable_path": "chromedriver.exe"}
    #browser = Browser("chrome", **executable_path, headless=False)

    featured_img_pg_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_img_pg_url)

    slice_object = slice(24)
    featured_img_pg_url = featured_img_pg_url[0:24]
    featured_img_pg_url

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    target_url = soup.find('footer')
    link_portion = target_url.a['data-fancybox-href']
    
    # ### Featured Image URL
    featured_image_url = (featured_img_pg_url.strip()) + link_portion
    print(f'The URL string for the featured image is {featured_image_url}')
    
    

    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser

    # executable_path = {"executable_path": "chromedriver.exe"}
    # browser = Browser("chrome", **executable_path, headless=False)


    
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(twitter_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    mars_weather = soup.find('span', class_='css-901oao css-16my406').text
    print(mars_weather)
    
    

# import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# from splinter import Browser
# import time

# executable_path = {"executable_path": "chromedriver.exe"}
# browser = Browser("chrome", **executable_path, headless=False)

    import pandas as pd
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    
    # ### Mars Fact Table
    fact_table = pd.read_html(facts_url)
    fact_table_df = fact_table[0]
    fact_table_df.columns=["Description", "Value"]
    fact_table_df = fact_table_df.drop([0])
    fact_table_df.set_index("Description", inplace=True)
    fact_table_df

    table_html = fact_table_df.to_html()
    print(table_html)

    
    

# ## Mars Hemispheres
# from bs4 import BeautifulSoup
# import requests
# from splinter import Browser
# import time

# executable_path = {"executable_path": "chromedriver.exe"}
# browser = Browser("chrome", **executable_path, headless=False)


    USGS_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    html = browser.html
    browser.visit(USGS_url)
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    html = browser.html
    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    url_list = soup.find_all('div', class_="item")
    print(url_list)

    root_url = "https://astrogeology.usgs.gov"
    hemisphere_img_urls = []

    for url in url_list:
        title = url.find('h3').text
        img_search_url = url.find('a', class_="itemLink product-item")['href']   
        browser.visit(root_url + img_search_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        #     print(soup.prettify())
    
        img_url = root_url + soup.find('img', class_="wide-image")["src"]
        #     print(img_url)
    
        hemisphere_img_urls.append({"Title" : title, "Image_URL" : img_url})
        hemisphere_img_urls

    print("Hemisphere Image URLs")
    print("---------------------")
    print(f'{hemisphere_img_urls[0]}')
    print()
    print(f'{hemisphere_img_urls[1]}')
    print()      
    print(f'{hemisphere_img_urls[2]}')
    print()
    print(f'{hemisphere_img_urls[3]}')     

    scraped_data = {
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "table_html": table_html,
        "hemisphere_img_urls": hemisphere_img_urls
        }

    browser_quit()
    return scraped_data