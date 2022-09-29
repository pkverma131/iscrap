import scrapy
import re

class ScreenerSpider(scrapy.Spider):
        name = "tickertape"
        def start_requests(self):
                urls = ['https://www.tickertape.in/stocks/reliance-industries-RELI?checklist=basic']
                for url in urls:
                        yield scrapy.Request(url=url, callback=self.parse)
        def parse(self, response):
                for stats_table in response.css('.stat-table-wrapper table'):
                    # Stats Title
                    stats_title_as = stats_table.css('table thead tr th')
                    stats_titles = [thead.css('span span::text').get() for thead in stats_title_as]
                    # Stats Value
                    stats_values = stats_table.css('table tbody tr td::text').getall()
                    yield {'stats_titles':stats_titles,'stats_values':stats_values}

