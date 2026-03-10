import scrapy

class SpiderTest(scrapy.Spider):
    name = "tattoodo"
    start_urls = ["https://www.tattoodo.com/", "https://tattooton.com/", "https://customtattoodesign.ca/home"]

    def parse(self, response):
        for res in response.xpath("//div[@class='FePjN8X']"):
            h1 = res.xpath(".//h1[@class='SXncH2d']/text()").get()
            p = res.xpath(".//p[@class='fsYUQZA']/text()").get()

        for quote in response.xpath("//div[@class='pmAHiQ0']"):
            a = quote.xpath(".//div[@class='Y5EYRZy']/a/@href").extract()

            if a:
                print(1111)
                yield response.follow(a[0], callback=self.parse_second_page)
                print("aaaa")

    def parse_second_page(self, response):
        for quote in response.xpath("//div[@class='dX63huH']"):
            p1 = quote.xpath(".//p[@class='wBsdqXy']/text()").get()
            yield {'SECOND PAGE': p1}
