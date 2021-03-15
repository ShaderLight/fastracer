import logging
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.INFO)

game_url = input("Enter game url: ")

browser = Chrome()
logging.info("Chromedriver initialised")

browser.get(game_url)
logging.info("Get request sent")

race_button = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'raceAgainLink')))
logging.info("Waiting for join button")

logging.info("Joining in 3")
for i in range(2,-1,-1):
    sleep(1)
    logging.info(str(i))

race_button.click()
logging.info("Joining...")


input("Press enter after game starts")

text_container = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'inputPanel')))
game_text = text_container.text
print(game_text)

input_box = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'txtInput')))

for character in game_text:
    input_box.send_keys(character)