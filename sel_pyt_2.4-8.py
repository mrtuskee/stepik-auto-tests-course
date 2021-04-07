from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

button = browser.find_element_by_id('book')
buttonwait = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button.click()


val1 = browser.find_element_by_id('input_value')
x = int(val1.text)
y = str(math.log(abs(12*math.sin(int(x)))))

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

done = browser.find_element_by_css_selector('#solve')
done.click()

time.sleep(10)

browser.quit()
