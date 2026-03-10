import scrapy
import json
import pandas as pd

# Define a Scrapy Spider class for crawling tattoo designs.
class Best_Tattoo_Design_Spider(scrapy.Spider):
    # Name of the spider.
    name = "tattooton"
    
    # The starting URL for the spider.
    start_urls = ["https://tattooton.com/"]

    # User agent string to be used in the request header.
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

    # Method for parsing the response from the start URL.
    def parse(self, response):
        # Loop through each navigation element found on the page.
        for nav_el in response.css('div.menu-home-container ul.sf-menu li a::attr(href)').extract():
            if nav_el:
                # Follow each navigation link and call the parse_nav_el method.
                yield response.follow(
                    nav_el,
                    callback=self.parse_nav_el
                )
            # Print the navigation element's URL to the console (for debugging).
            print(nav_el)

    # Method for parsing each navigation element.
    def parse_nav_el(self, response):
        # Loop through each article found on the navigation page.
        for article in response.css('div.td-module-thumb'):
            # Extract the title of the article.
            article_title = article.css('a::attr(title)').get()
            # Extract the link to the article.
            article_link = article.css('a::attr(href)').get()
            # Follow the link to the article and call the parse_article method.
            yield response.follow(
                article_link,
                callback=self.parse_article,
                meta={'docno': article_title, 'link': article_link}
            )
    
    # Method for parsing individual articles.
    def parse_article(self, response):
        # Retrieve the title and link of the article from the response's metadata.
        title = response.meta['docno']
        link = response.meta['link']
        text = ""

        # Concatenate all paragraph text from the article.
        for p in response.css('p::text'):
            text += p.get().strip() + " "
        
        # Yield the article data as a dictionary.
        yield {
            'docno': title,
            'link': link,
            'text': text,
        }
