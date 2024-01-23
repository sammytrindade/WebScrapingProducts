from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def webdriver_configurations():
    service = Service()
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(service=service, options=options)
