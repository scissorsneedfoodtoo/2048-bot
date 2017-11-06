#!/usr/bin/python3
# 2048-bot - Plays 3 rounds of 2048 and tracks the current game's score, and the top
# score from the 3 game session

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://gabrielecirulli.github.io/2048/')
time.sleep(3)
noticeButton = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".notice-close-button"))
)
# print(noticeButton.text)

# For now the easiest way to close the popup is to wait for it to open
# time.sleep(5)
# noticeButton = driver.find_element_by_css_selector('.notice-close-button')
noticeButton.click()



# print(random.randint(0, 3)) # random number for random arrow key press
