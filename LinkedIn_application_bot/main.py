from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "/Users/dillonjohn/Sites/chromedriver-3"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)



URL = "https://www.linkedin.com/jobs/search/?currentJobId=2748031614&f_" \
      "AL=true&f_PP=102571732%2C102277331%2C104116203&f_WT=2&geoId=103644278&" \
      "keywords=software%20engineer&location=United%20States&sortBy=R"


driver.get(URL)

sign_in = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')

sign_in.click()

usrnme= os.getenv("USERNAME")
username = driver.find_element_by_id("username")
username.send_keys()

pswrd = os.getenv("PASSWORD")
password = driver.find_element_by_id("password")
password.send_keys(pswrd)

sign_in = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()

time.sleep(5)

click_job = driver.find_element_by_css_selector(".jobs-apply-button--top-card")
click_job.click()


click_next = driver.find_element_by_css_selector('.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
click_next.click()
click_next.click()



click_yes = driver.find_element_by_css_selector('#radio-urn\:li\:fs_easyApplyFormElement\:\(urn\:li\:fs_normalized_jobPosting\:2748031614\,35662795\,multipleChoice\)_0')
# Useful for clicking item that shares properties with others
webdriver.ActionChains(driver).move_to_element(click_yes ).click(click_yes ).perform()

# Fills in questions
exp1 =driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2748031614,35662803,numeric)"]')
exp1.send_keys("1")

exp2 =driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2748031614,35662779,numeric)"]')
exp2.send_keys("1")

exp3 =driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2748031614,35662787,numeric)"]')
exp3.send_keys("1")

click_next = driver.find_element_by_css_selector('.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
click_next.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

click_next = driver.find_element_by_css_selector('.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
click_next.click()

# X button for after submitting
driver.find_element_by_css_selector('.artdeco-modal__dismiss.artdeco-button artdeco-button--circle artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view')
# time.sleep(30)
# driver.quit()