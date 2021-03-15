import logging

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

game_url = input("Enter game url: ")

browser = Chrome()
logging.debug("Chromedriver initialised")

browser.get(game_url)
logging.debug("Get request sent")

logging.debug("Waiting for join button")
race_button = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'raceAgainLink')))

race_button.click()
logging.info("Joining...")

input("Press enter after the game starts")

text_container = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'inputPanel')))
game_text = text_container.text
logging.debug("Text panel found, text scrapped")

input_box = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'txtInput')))

logging.debug("Input panel detected, sending inputs...")
for character in game_text:
    input_box.send_keys(character)