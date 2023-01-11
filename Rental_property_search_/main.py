from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "/Users/dillonjohn/Sites/chromedriver-3"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

POLL_URL = "https://docs.google.com/forms/d/e/1FAIpQLScRCi7B3" \
           "Z6BzVtPb4CeO9umltSL3K5e4L4nDDSF_9a38fqe2Q/" \
           "viewform?usp=sf_link"

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3" \
             "Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.6926134523046" \
             "7%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%" \
             "22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3" \
             "A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%2" \
             "2%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%2" \
             "2%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


driver.get(ZILLOW_URL)

location_name = input("Enter full city name followed by comma and state abbreviation EX: New York, NY")

location = driver.find_element(By.XPATH, '//*[@id="__c11n_fq416pfw"]')
location.send_keys(location_name)

rent_button1 = driver.find_element(By.XPATH, '//*[@id="listing-type"]')
rent_button1.click()

time.sleep(3)
rent_button2 = driver.find_element(By.XPATH, '//*[@id="__c11n_lkh2k"]/span')
rent_button2.click()

price_button1 = driver.find_element(By.XPATH, '//*[@id="price"]')
price_button1.click()

price_min = input("Enter the minimum price you are willing to pay:")
price_minbox = driver.find_element(By.XPATH, '//*[@id="price-exposed-min"]')
price_minbox.send_keys(price_min)

price_max = input("Enter the maximum price you are willing to pay:")
price_maxbox = driver.find_element(By.XPATH, '//*[@id="price-exposed-max"]')
price_maxbox.clear()
price_maxbox.send_keys(price_max)

price_popup_close = driver.find_element(By.XPATH, '//*[@id="search-page-react-content"]/section/div[2]/div/div[2]/div/div/div/button')
price_popup_close.click()

search_submit = driver.find_element(By.XPATH, '//*[@id="__c11n_fq416pfy"]/button')
search_submit.click()

search_url = driver.current_url


soup = BeautifulSoup(search_url,'html.parser')

soup.find_all()




