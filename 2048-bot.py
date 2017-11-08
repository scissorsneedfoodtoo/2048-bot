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

# Wait for popup and close it
try:
    noticeButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.notice-close-button'))
    )
finally:
    time.sleep(.5) # Needs a brief moment before clicking, otherwise it will misclick
    noticeButton.click()

def playGame(gameRound):
    gameOver = False
    body = driver.find_element_by_css_selector('body')

    # random number for random arrow key press
    randomNumber = random.randint(0, 3)
    keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

    while not gameOver and gameRound <= 3:
        try:
            gameOver = driver.find_element_by_css_selector('.game-message.game-over')
            return finishGame(gameRound)
        except NoSuchElementException:
            body.send_keys(random.choice(keys))
            time.sleep(.005)

def finishGame(gameRound):

    # sleep so the score-addition class isn't captured
    time.sleep(1)

    roundScore = driver.find_element_by_css_selector('.score-container').text
    topScore = driver.find_element_by_css_selector('.best-container').text

    print('Round {} is over!'.format(gameRound))
    print('The score this round is {}, and the top score is {}.'.format(roundScore, topScore))

    gameRound += 1

    if gameRound <= 3:
        restartButton = driver.find_element_by_css_selector('.retry-button')

        restartButton.click()
        return playGame(gameRound)
    else:
        print('Game over!')

gameRound = 1

playGame(gameRound)
