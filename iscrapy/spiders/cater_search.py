import scrapy
from scrapy_selenium import SeleniumRequest

class CaterSearchSpider(scrapy.Spider):
        name = "cater_search"
        def start_requests(self):
                url = 'https://www.google.com/maps/search/catering+service/@26.8696937,80.9685845,12z/data=!3m1!4b1'
                yield SeleniumRequest(
                        url = url,
                        wait_time = 3,
                        screenshot = True,
                        callback = self.parse,
                        dont_filter = True
                    )
        def parse(self, response):
            for href in response.xpath('.//a'):
                yield {'href':href.get()}

