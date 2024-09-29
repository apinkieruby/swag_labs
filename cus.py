import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# set up the browser
driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()