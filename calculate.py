from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW

from time import sleep, perf_counter

url = 'https://litarweb.lrmuitine.lt/taric/web/securitycalc_EN'
url_usd = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&newwindow=1&sxsrf=APwXEddmIRvHcsq3L2-rwnzuss3WoEaQkg%3A1687513826459&ei=4mqVZMvIG8WL9u8PicyGkAo&ved=0ahUKEwjLwbfxjtn_AhXFhf0HHQmmAaIQ4dUDCA8&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzINCAAQigUQsQMQgwEQQzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoGCAAQBxAeOgcIABCKBRBDSgQIQRgAUABY1ghgmRVoAHABeACAAZgBiAHVBJIBAzQuMpgBAKABAcABAQ&sclient=gws-wiz-serp'
url_rub = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&newwindow=1&sxsrf=APwXEdc-UHdIwjl_cIJ5Ukf30JQli9JmRA%3A1687513875190&ei=E2uVZOSZC5uC9u8P6PyeuAQ&ved=0ahUKEwik79WIj9n_AhUbgf0HHWi-B0cQ4dUDCA8&uact=5&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIMCCMQigUQJxBGEIICMgcIABCKBRBDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BggAEAcQHjoHCCMQigUQJzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOg0IABCKBRCxAxCDARBDOgoIABCABBAUEIcCOgcIABCABBAKSgQIQRgASgQIQRgAUABYhX5ggIIBaAFwAXgAgAHSAYgB2w2SAQYwLjEzLjGYAQCgAQGwARTAAQHaAQYIARABGAE&sclient=gws-wiz-serp'
chrome_service = ChromeService('chromedriver.exe')
chrome_service.creation_flags = CREATE_NO_WINDOW
option_chrome = webdriver.ChromeOptions()
option_chrome.add_argument('--window-size=1920,1080')
option_chrome.add_argument('--no-sandbox')
option_chrome.add_argument('--headless')
option_chrome.add_argument('--disable-gpu')
option_chrome.add_argument('--disable-crash-reporter')
option_chrome.add_argument('--disable-extensions')
option_chrome.add_argument('--disable-in-process-stack-traces')
option_chrome.add_argument('--disable-logging')
option_chrome.add_argument('--disable-dev-shm-usage')
option_chrome.add_argument('--log-level=3')
option_chrome.add_argument('--log-path=/dev/null')

option_chrome.add_argument('--disable-dev-shm-usage')



def calculate(code, mass, value, country):
    browser = webdriver.Chrome(service=chrome_service, options=option_chrome)


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
    # sleep(10)
    # goods_code = browser.find_element(By.ID, 'goods_code').text
    goods_code = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, 'goods_code'))).text
    tax_result = browser.find_element(By.ID, 'tax_result').text
    message = browser.find_element(By.ID, 'messages_table_body').text
    table_row = [i.split() for i in browser.find_element(By.ID, "measure_table_body").text.split('\n')]
    table_headers = [i.text for i in browser.find_elements(By.TAG_NAME, 'th')]

    browser.quit()

    return message, goods_code, tax_result, table_row, table_headers
