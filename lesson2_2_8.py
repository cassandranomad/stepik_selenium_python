from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Smolensk")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'fileeee.txt')           # добавляем к этому пути имя файла 
    input4 = browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(30)
    browser.quit()




