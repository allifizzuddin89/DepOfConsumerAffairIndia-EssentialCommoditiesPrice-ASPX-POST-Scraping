import scrapy
from scrapy import FormRequest
from scrapy.shell import inspect_response

class MainSpider(scrapy.Spider):
    name = 'main'
    #allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
