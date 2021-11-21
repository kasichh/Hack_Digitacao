import time

import selenium.webdriver.chrome.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.keybr.com/')
sleep(2)
driver.find_element(By.CLASS_NAME, 'X6jBH4QQC438WF7fZYzD').click()
# letras = driver.find_elements(By.XPATH, '//div[contains (@class, "pklLOFTYXcQTUpcTaOg7")]/span')
# campo = driver.find_element(By.CLASS_NAME, 'pklLOFTYXcQTUpcTaOg7')
# driver.find_element(By.XPATH, '//div[contains (@class, "pklLOFTYXcQTUpcTaOg7")]').click()
pyautogui.moveTo(886, 513)
pyautogui.click()
letras = driver.find_elements(By.XPATH, '//div[contains (@class, "pklLOFTYXcQTUpcTaOg7")]/span')
time.sleep(1)
lista = list()

for palavra in letras:
    letra = palavra.text
    if letra == '␣':
        letra = 'space'
    lista.append(str(letra))

for letra in lista:
    pyautogui.press(letra)





