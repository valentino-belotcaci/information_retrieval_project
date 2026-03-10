import scrapy


class Best_Tattoo_Design_Spider(scrapy.Spider):
    # Set the name of the spider
    name = "tattoodo"

    # Define the starting URL for the spider
    start_urls = ["https://www.tattoodo.com/articles"]

    # Define a user agent to be used in the HTTP request headers
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

    # Main parsing method
    def parse(self, response):
        # Extract articles from the first type of container
        for article in response.css('div.ZUJYgWF'):
            # Extract the title and link of the article
            article_title = article.css('img::attr(alt)').get()
            article_link = 'https://www.tattoodo.com' + article.css('a::attr(href)').get()

            # Follow the link to the article and call the parse_article method
            yield response.follow(
                article_link,
                callback=self.parse_article,
                meta={'docno': article_title, 'link': article_link}
            )

        # Extract articles from the second type of container
        for article in response.css('div.lMEUwJR div.Ois1KYc section.yAzztne'):
            # Extract the title and link of the article
            article_title = article.css('img::attr(alt)').get()
            article_link = 'https://www.tattoodo.com' + article.css('a::attr(href)').get()

            # Follow the link to the article and call the parse_article method
            yield response.follow(
                article_link,
                callback=self.parse_article,
                meta={'docno': article_title, 'link': article_link}
            )

        # Extract articles from the third type of container
        for article in response.css('section.h4jG6nA'):
            # Extract the title and link of the article
            article_title = article.css('img::attr(alt)').get()
            article_link = 'https://www.tattoodo.com' + article.css('a::attr(href)').get()

            # Follow the link to the article and call the parse_article method
            yield response.follow(
                article_link,
                callback=self.parse_article,
                meta={'docno': article_title, 'link': article_link}
            )

    # Method to parse individual articles
    def parse_article(self, response):
        # Retrieve metadata from the meta attribute
        title = response.meta['docno']
        link = response.meta['link']
        text = ""

        # Extract text content from paragraphs in the article
        for p in response.css('div.VMkhrqp p::text'):
            text += p.get().strip() + " "

        # Yield a dictionary with the extracted data
        yield {
            'docno': title,
            'link': link,
            'text': text,
        }
