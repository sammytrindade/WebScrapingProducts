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

