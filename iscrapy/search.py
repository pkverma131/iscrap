import scrapy
import selenium
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Search:
    def __init__(self):
        self.PATH = "/home/pydev/reproject/tutorial/tutorial/chromedriver"
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service('/home/pydev/reproject/tutorial/tutorial/chromedriver'),options=webdriver.ChromeOptions())
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def scrape(self):
        self.driver.get('https://www.google.com/maps/search/catering+service/@26.8696937,80.9685845,12z/data=!3m1!4b1') 
        scrapy_selector = Selector(text = self.driver.page_source)
        html_links = scrapy_selector.xpath('//body//a')
        print(html_links)

s = Search()
s.scrape()