from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW

from time import sleep

url = 'https://litarweb.lrmuitine.lt/taric/web/securitycalc_EN'

chrome_service = ChromeService()
chrome_service.creation_flags = CREATE_NO_WINDOW
option_chrome = webdriver.ChromeOptions()
option_chrome.add_argument('--headless=old')
option_chrome.add_argument('--window-size=1920,1080')
option_chrome.add_argument('--no-sandbox')
option_chrome.add_argument('--disable-gpu')
option_chrome.add_argument('--disable-crash-reporter')
option_chrome.add_argument('--disable-extensions')
option_chrome.add_argument('--disable-in-process-stack-traces')
option_chrome.add_argument('--disable-logging')
option_chrome.add_argument('--disable-dev-shm-usage')
option_chrome.add_argument('--log-level=3')
option_chrome.add_argument('--log-path=/dev/null')

def calculate(code, mass, value, country):

    browser = webdriver.Chrome(service=chrome_service, options=option_chrome)
    sleep(0.5)
    browser.get(url)
    sleep(0.5)

    wb_search_1 = browser.find_element(By.ID, 'commodity_code')
    wb_search_1.send_keys(code)

    wb_search_2 = browser.find_element(By.ID, 'net_mass')
    wb_search_2.send_keys(mass)

    wb_search_3 = browser.find_element(By.ID, 'statistical_value')
    wb_search_3.send_keys(value)

    wb_search_4 = browser.find_element(By.ID, 'country_region')
    wb_search_4.send_keys(country)

    browser.find_element(By.ID, 'submit_button').click()

    goods_code = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'goods_code'))).text
    tax_result = browser.find_element(By.ID, 'tax_result').text
    message = browser.find_element(By.ID, 'messages_table_body').text
    table_row = [i.split() for i in browser.find_element(By.ID, "measure_table_body").text.split('\n')]
    table_headers = [i.text for i in browser.find_elements(By.TAG_NAME, 'th')]

    browser.close()
    browser.quit()
    return message, goods_code, tax_result, table_row, table_headers


