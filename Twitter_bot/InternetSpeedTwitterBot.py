import time
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os


class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        self.chrome_driver_path = Service("/Users/dillonjohn/Sites/chromedriver-3")
        self.options = Options()
        self.options.add_argument("--kiosk")
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=self.chrome_driver_path, options=self.options)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(60)
        try:
            download_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                      "result-data-large.number.result-data-value.download-speed")
            upload_speed = self.driver.find_element(By.CSS_SELECTOR,
                                                    "result-data-large.number.result-data-value.upload-speed")

            # self.driver.quit()

            return f"Download Speed:{download_speed}\nUpload Speed:{upload_speed}"
        except NoSuchElementException:
            exit_popup = self.driver.find_element(By.CLASS_NAME, "main-content")
            exit_popup.click()
            time.sleep(10)
            download_speed = self.driver.find_element(By.XPATH,
                                                      '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            upload_speed = self.driver.find_element(By.XPATH,
                                                    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

            # time.sleep(5)
            # self.driver.quit()
            return f"Download Speed:{download_speed.text}\nUpload Speed:{upload_speed.text}"

    def tweet_at_provider(self):
        self.driver.get("twitter.com")
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
        sign_in_button.click()
        time.sleep(5)
        user_name_input = self.driver.find_element(By.CSS_SELECTOR,
                                                   "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj."
                                                   "r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        user_name_input.send_keys(os.getenv("USERNAME"))
        user_name_input.send_keys(Keys.ENTER)
        password_input = self.driver.find_element(By.CSS_SELECTOR,
                                                  "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj."
                                                  "r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        password_input.send_keys(os.getenv("PASSWORD"))
        password_input.send_keys(Keys.ENTER)

        time.sleep(10)
        post_input = self.driver.find_element(By.CSS_SELECTOR,
                                              "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        post_input.click()
        post_input.send_keys(f"My internet speed is {self.get_internet_speed()}")
        post_input.send_keys(Keys.ENTER)
        return
