"""

nse_attempt_01.py

(resource "http://scrapy.org/")

"""
import scrapy


class NSESpider(scrapy.Spider):
    """
    NSESpider

    """
    name = 'nsespider'
    start_urls = ['https://www.nse.co.ke/market-statistics/market-snapshot.html']

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
