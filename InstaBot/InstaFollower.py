from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
# import WebDriverWait
import time
import os


CHROME_DRIVER_PATH = "/Users/dillonjohn/Sites/chromedriver-3"
TARGET_ACCOUNT = os.getenv("TARGET_ACCOUNT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = "https://www.instagram.com"
URL2 = f"https://www.instagram.com/{TARGET_ACCOUNT}/"

class InstaFollower:
    def __init__(self):
        self.chrome_driver_path = Service(CHROME_DRIVER_PATH)
        self.options = Options()
        self.options.add_argument("--kiosk")
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.chrome_driver_path, options=self.options)
        self.driver.get(URL)


    def login(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".input._2hvTZ.pexuQ.zyHYP")
        login_button.send_keys(USERNAME)
        password_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Password")
        password_button.send_keys(PASSWORD)
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "sqdOP.L3NKy.y3zKF")
        submit_button.click()
        time.sleep(5)
    def find_followers(self):
        self.driver.get(URL2)

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
