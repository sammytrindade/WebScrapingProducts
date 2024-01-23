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


def get_total_pages(driver):
    try:
        pagination = driver.find_element(By.CLASS_NAME, 'catalog-footer')
        pages = pagination.find_elements(By.CLASS_NAME, 'page')
        return len(pages) - 1
    except NoSuchElementException:
        return 0


def navigate_to_page(driver, category_link, page_number):
    try:
        if '?' in category_link:
            page_link = f"{category_link}&pg={page_number}"
        else:
            page_link = f"{category_link}?pg={page_number}"

        driver.get(page_link)
        sleep(2) 
    except Exception as e:
        print(f"Erro ao navegar para a página {page_number}: {e}")
