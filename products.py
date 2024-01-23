from webdriver_setup import webdriver_configurations
from selenium.webdriver.common.by import By
from time import sleep
from pagination_utils import check_pagination, has_products, get_total_pages, navigate_to_page
from table_utils import print_table
from time import sleep
from selenium.webdriver.common.by import By
from table_utils import create_table
from screenshot_utils import take_screenshot
from datetime import datetime


def showDateAndHour():
    """Esta função retorna data e hora atual"""
    today = datetime.now()
    hour = today.strftime("%H:%M:%S")
    date = today.strftime("%d-%m-%Y")
    return date, hour


def get_product_details(driver, product_link):
    driver.get(product_link)
    sleep(3)

    product_name_element = driver.find_element(By.CLASS_NAME, 'product-name')
    product_name = product_name_element.text.strip()

    product_price_element = driver.find_element(By.ID, 'variacaoPreco')
    product_price = product_price_element.text.strip()

    currency_element = driver.find_element(By.CLASS_NAME, 'currency')
    currency = currency_element.text.strip()

    product_code_element = driver.find_element(By.ID, 'product-reference')
    product_code = product_code_element.text.strip()
    return product_name, product_price, currency, product_code


def process_products(driver, products, data_df):
    products_links = []
    for product in products:
        href_products = product.find_element(
            By.CSS_SELECTOR, '.product-body .product-info')
        product_link = href_products.get_attribute('href')
        products_links.append(product_link)
    for product_link in products_links:
        print(f"Navegando para o produto: {product_link}")
        current_page_url = driver.current_url
        driver.get(product_link)
        sleep(2)

        product_name, product_price, currency, product_code = get_product_details(
            driver, product_link)
        date, hour = showDateAndHour()
        screenshot_filename = take_screenshot(product_code, product_name, date)
        table = create_table(product_name, product_code, product_price,
                             currency, product_link, date, screenshot_filename)
        data_df.append(table)
        driver.get(current_page_url)
        sleep(2)

