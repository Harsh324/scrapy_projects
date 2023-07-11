import scrapy
from quotestoscrape.items import QuotestoscrapeItem

class ScrapitSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):
        item = QuotestoscrapeItem()
        #item['title'] = response.css('title').extract()

        yield {'titletext' : response.css('title::text').getall()}