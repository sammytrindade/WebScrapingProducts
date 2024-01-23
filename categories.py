from selenium.webdriver.common.by import By
from webdriver_setup import webdriver_configurations
driver = webdriver_configurations


def get_categories(driver, url):
    driver.get(url)
    categories = driver.find_elements(
        By.CSS_SELECTOR, 'ul.list.flex.justify-center a')

    all_links = []
    name_category = []

    for category in categories:
        title_value = category.get_attribute('title')
        if title_value == category.text:
            link_by_category = category.get_attribute('href')
            name_category.append(title_value)
            all_links.append(link_by_category)

    return name_category, all_links
