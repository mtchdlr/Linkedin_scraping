import selenium
from selenium import webdriver
import bs4
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementNotSelectableException, \
    ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import re
import pandas as pd
import requests
import time
import numpy as np
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = Service('C:\\Users\dmchedluri\Desktop\chromedriver_90.0.4430.24\chromedriver.exe')
driver = webdriver.Chrome(service = path)

driver.get('https:/linkedin.com')
driver.maximize_window()

wait = WebDriverWait(driver, 10,  poll_frequency=1)

mail = driver.find_element(By.XPATH, '//*[@id="session_key"]')
action_1 = ActionChains(driver)
action_1.move_to_element(mail).click().send_keys('david.mtchedluri@iset.ge').perform()

time.sleep(2)

password = driver.find_element(By.XPATH,'//*[@id="session_password"]')
action_2 = ActionChains(driver)
action_2.move_to_element(password).click().send_keys('Linked.1996').perform()

time.sleep(2)

sign_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
action_3 = ActionChains(driver)
action_3.move_to_element(sign_in).click().perform()

time.sleep(2)

wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/header/div/div/div/div[1]/input')))
search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
action_4 = ActionChains(driver)
action_4.move_to_element(search).click().send_keys('data scientist').perform()
webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(2)
