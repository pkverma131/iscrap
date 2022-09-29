from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_service_providers(url2):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    caters = []
    try: 
        driver.get(url2) 
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        cater_lnks=driver.find_elements(By.CSS_SELECTOR, "a")
        caters = [cater_lnk.get_attribute('href') for cater_lnk in cater_lnks if 'https://www.google.com/maps/place' in str(cater_lnk.get_attribute('href'))]
    except Exception as e:
        driver.quit()
    finally:
        driver.quit() 
    return caters

def get_service_provider_details(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    cater_details = {}
    try: 
        driver.get(url) 
        time.sleep(10)
        cater_details['address'] = driver.find_element(By.CSS_SELECTOR, "[data-item-id='address']").text
        cater_details['phone_number'] = driver.find_element(By.CSS_SELECTOR, "[data-tooltip='Copy phone number']").text
        cater_details['website'] = driver.find_element(By.CSS_SELECTOR, "[data-item-id='authority']").text
    except Exception as e:
        driver.quit()
    finally:
        driver.quit() 
    return cater_details
def get_service_provider_list():
    service_provider_list = []
    url2 = "https://www.google.com/maps/search/transport+service/@26.860897,81.0020575,15z"
    # url2 = "https://www.google.com/maps/search/catering+service/@26.860897,81.0020575,15z"
    service_providers = get_service_providers(url2)
    print(len(service_providers))
    print(service_providers)
    # time.sleep(10)
    for url in service_providers:
        service_provider_details = get_service_provider_details(url)
        print(service_provider_details)
        service_provider_list.append(service_provider_details)
    return service_provider_list

get_service_provider_list()