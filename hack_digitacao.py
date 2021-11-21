import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.keybr.com/')
sleep(2)
driver.find_element(By.CLASS_NAME, 'X6jBH4QQC438WF7fZYzD').click()
valores = driver.find_element(By.CLASS_NAME, 'pklLOFTYXcQTUpcTaOg7')


