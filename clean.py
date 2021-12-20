# import selenium
from selenium import webdriver
# import bs4
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
# import re
import pandas as pd
# import requests
import time
# import numpy as np
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

georgian_last_names = pd.read_csv('georgian_last_names.csv', header = [0])
last_names = georgian_last_names.Georgian_last_names.to_list()

path = Service('C:\\Users\dmchedluri\Desktop\chromedriver_90.0.4430.24\chromedriver.exe')
driver = webdriver.Chrome(service = path)

driver.get('https:/linkedin.com')
driver.maximize_window()
wait = WebDriverWait(driver, 10,  poll_frequency=1)


mail = driver.find_element(By.XPATH, '//*[@id="session_key"]')
action_1 = ActionChains(driver)
action_1.move_to_element(mail).click().send_keys('mayatushuri@gmail.com').perform()
time.sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
action_2 = ActionChains(driver)
action_2.move_to_element(password).click().send_keys('Li_nked_In_1996').perform()
time.sleep(2)
sign_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
action_3 = ActionChains(driver)
action_3.move_to_element(sign_in).click().perform()
time.sleep(2)


search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
action_4 = ActionChains(driver)
action_4.move_to_element(search).click().send_keys('data scientist').perform()
webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(1)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2)


# Clicking on People
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-reusables__filter-pill-button')))
filter_tabs = driver.find_elements(By.CSS_SELECTOR, '.search-reusables__filter-pill-button')

for i in range(0, int(len(filter_tabs))+1):
    if 'People' in filter_tabs[i].text:
        action_5 = ActionChains(driver)
        action_5.move_to_element(filter_tabs[i]).click().perform()
        break
    else:
        continue

# Clicking on Location
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-reusables__filter-pill-button')))
filter_tabs = driver.find_elements(By.CSS_SELECTOR, '.search-reusables__filter-pill-button')

for i in range(0, len(filter_tabs)+1):
    if 'Locations' in filter_tabs[i].text:
        action_6 = ActionChains(driver)
        action_6.move_to_element(filter_tabs[i]).click().perform()
        break
    else:
        continue

time.sleep(1.5)
location_input_box_child = driver.find_element(By.XPATH, '//input[@placeholder="Add a location"]')
location_input_box = location_input_box_child.find_element(By.XPATH, '..')

action_7 = ActionChains(driver)
action_7.move_to_element(location_input_box).click().send_keys('United Kingdom').perform()

# Choosing a country
time.sleep(3)
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'basic-typeahead__triggered-content')))
parent_elem = driver.find_element(By.CLASS_NAME, 'basic-typeahead__triggered-content')
child_elements = parent_elem.find_elements(By.XPATH, './/*')[1]
time.sleep(1.5)
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
ActionChains(driver).move_to_element(child_elements).click().perform()
time.sleep(1.5)

# Show_Results Button
show_results_button = driver.find_element(By.CLASS_NAME, 'artdeco-button__text')
ActionChains(driver).move_to_element(show_results_button).click().perform()
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


# while loop, scarping each page for names
# empty dataframe
df = pd.DataFrame(columns=['name', 'location', 'position', 'current/past'])
data = {}

while True:
    time.sleep(2)
    guys = driver.find_elements(By.CLASS_NAME, 'reusable-search__result-container ')
    for guy in range(1, len(guys)+1):
        check_last_name = driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')[0].text
        if check_last_name.split[1] in last_names:
            try:
                if len(driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]')) > 0:
                     data['name'] = driver.find_element(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                elif len(driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')) > 0:
                    data['name'] = driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a')[0].text
                else:
                    print('NA')
            except:
                continue

            try:
                data['location'] = driver.find_element(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
            except:
                data['location'] = 'NA'

            try:
                data['position'] = driver.find_element(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[1]/div[2]/div/div[1]').text
            except:
                data['position'] = 'NA'

            try:
                data['current/past'] = driver.find_element(By.XPATH, f'//*[@id="main"]/div/div/div[2]/ul/li[{guy}]/div/div/div[2]/div[2]/p').text
            except:
                data['current/past'] = 'NA'
            df = df.append(data, ignore_index=True)
        else:
            continue
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Next"]')))
        next = driver.find_elements(By.XPATH, '//button[@aria-label="Next"]')
        ActionChains(driver).move_to_element(next[0]).click().perform()
        time.sleep(4)
    except:
        break

print('Scraping is finished')
df.to_csv('C:\\Users\\dmchedluri\\Desktop\\linkedin\\Linkedin_scraping-main\\df.csv')