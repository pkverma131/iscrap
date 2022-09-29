import scrapy
import re

class ScreenerSpider(scrapy.Spider):
        name = "Screener"
        def start_requests(self):
                urls = ['https://www.screener.in/company/INFY/consolidated/']
                for url in urls:
                        yield scrapy.Request(url=url, callback=self.parse)
        def parse(self, response):
                top_ratios = []
                for ratio in response.css('#top-ratios li'):
                        atrs = {re.sub(r"[\n\t\s]*","",ratio.css('span.name::text').get()):
                        re.sub(r"[\n\t\s]*","",str(ratio.css('span.nowrap::text').get()))
                        +re.sub(r"[\n\t\s]*","",str(ratio.css('span.nowrap span::text').get()))}
                        top_ratios.append(atrs)
                print(top_ratios)

