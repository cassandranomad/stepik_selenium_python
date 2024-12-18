from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button1 = browser.find_element(By.CSS_SELECTOR, '#book').click()
button2 = browser.find_element(By.CSS_SELECTOR, '#solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
button2 = browser.find_element(By.CSS_SELECTOR, '#solve').click()

time.sleep(5)
browser.quit()



