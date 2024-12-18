from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(z, y):
  return int(z) + int(y)

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    z_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    z = z_element.text
    y_elements = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = y_elements.text
    u = str(calc(z, y))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(u) 

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()