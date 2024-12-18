from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(30)
browser.quit()




