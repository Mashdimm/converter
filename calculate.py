from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
import time

def calculate(code: str, mass: str, value: str, country: str):

    url = "https://litarweb.lrmuitine.lt/portal/transitcalc"

    chrome_service = ChromeService()
    chrome_service.creation_flags = CREATE_NO_WINDOW

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=chrome_service, options=options)

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 2)
        short_wait = WebDriverWait(driver, 1)


        # Cookie
        try:
            cookie_btn = wait.until(EC.element_to_be_clickable((By.XPATH,
                '//*[@id="portal-982480788"]/vaadin-vertical-layout/vaadin-vertical-layout[3]/vaadin-vertical-layout/vaadin-horizontal-layout/vaadin-vertical-layout[2]/vaadin-button[1]'
            )))
            cookie_btn.click()
            time.sleep(1)
        except:
            pass

        # Код товара

        wait.until(EC.presence_of_element_located((By.ID, "input-vaadin-text-field-16"))).send_keys(code)

        # Кнопка NEXT

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//vaadin-button[contains(., 'Pirmyn')]"))).click()
        except:
            return "ERROR", None, None

        # Стоимость

        wait.until(EC.presence_of_element_located((By.ID, "input-vaadin-number-field-24"))).send_keys(value)

        # Страна

        try:
            combo = wait.until(EC.element_to_be_clickable((By.ID, "input-vaadin-combo-box-29")))
            combo.click()
            combo.send_keys(country)
            time.sleep(0.8)
            item = wait.until(EC.presence_of_element_located(
                (By.XPATH, f"//vaadin-combo-box-item[contains(text(), '{country}')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            driver.execute_script("arguments[0].click();", item)
        except:

            return "ERROR", None, None

        # Вес

        try:

            wait.until(EC.presence_of_element_located((By.ID, "input-vaadin-number-field-33"))).send_keys(mass)


        except:
            return "ERROR", None, None

        # Кнопка NEXT
        try:

            wait.until(EC.element_to_be_clickable((By.XPATH, "//vaadin-button[contains(., 'Pirmyn')]"))).click()
        except:
            return "ERROR", None, None

        # Ставка пошлины
        try:
            short_wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'vaadin-grid-cell-content[slot="vaadin-grid-cell-content-18"]')
            ))
            duty = driver.find_element(By.CSS_SELECTOR,
                'vaadin-grid-cell-content[slot="vaadin-grid-cell-content-18"]').text.strip()
        except:
            return "ERROR", None, None

        # Итоговая сумма расчёта
        try:

            short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2.section-title")))
            titles = driver.find_elements(By.CSS_SELECTOR, "h2.section-title")
            total = None
            for title in titles:
                if "Tranzito garantijos dydis" in title.text:
                    total = title.text.split(":")[1].replace("EUR", "").strip()
                    break
            if not total:
                return "ERROR", None, None
        except:
            return "ERROR", None, None

        return None, duty, total

    except Exception:
        return "ERROR", None, None
    finally:
        driver.quit()
