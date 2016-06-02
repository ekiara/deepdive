"""

first_example.py

(resource "http://scrapy.org/")

"""
import scrapy

class BlogScrapinghubSpider(scrapy.Spider):
    """
    BlogScrapinghubSpider
    """
    name = 'blogscrapinghubspider'
    start_urls = ['https://blog.scrapinghub.com']


    def parse(self, response):
        """
        parse

        """
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)


    def parse_titles(self, response):
        """
        parse_titles

        """
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}
