#!/usr/bin/python3
# 2048-bot - Plays 3 rounds of 2048 and tracks the current game's score, and the top
# score from the 3 game session

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import random

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://gabrielecirulli.github.io/2048/')

# wait for popup and close it
# time.sleep(2)
# noticeButton = driver.find_element_by_css_selector('body > div > div.app-notice > span')
# noticeButton = WebDriverWait(driver, 50).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, '.notice-close-button'))
# )
# noticeButton.click()

# try:
#     noticeButton = driver.find_element_by_css_selector('body > div > div.app-notice > span')
# except NoSuchElementException:
#     noticeButton = driver.find_element_by_css_selector('body > div > div.app-notice > span')
    # noticeButton = WebDriverWait(driver, 3).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, '.notice-close-button'))
    # )
    # noticeButton.click()

body = driver.find_element_by_css_selector('body')

# random number for random arrow key press
randomNumber = random.randint(0, 3)
keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

gameOver = False

while not gameOver:
    try:
        gameOver = driver.find_element_by_css_selector('body > div > div.game-container > div.game-message.game-over')
    except NoSuchElementException:
        body.send_keys(random.choice(keys))
        # time.sleep(.2)

if gameOver:
    # sleep so the score-addition class isn't captured
    time.sleep(1)

    roundScore = driver.find_element_by_css_selector('body > div > div.heading > div > div.score-container').text
    topScore = driver.find_element_by_css_selector('body > div > div.heading > div > div.best-container').text

    print('Game over!')
    print('The score this round is {}, and the top score is {}'.format(roundScore, topScore))
