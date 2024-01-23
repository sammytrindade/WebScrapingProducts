from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


def check_pagination(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'catalog-footer')
        return True
    except NoSuchElementException:
        return False


def has_products(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'catalog-empty')
        return False
    except NoSuchElementException:
        return True

