from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)   

    cena = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card-body #price"),'$100'))# ждем пока цена не будет равна 100
    button1 = browser.find_element_by_css_selector(".btn#book")
    button1.click()
    x_element = browser.find_element_by_id("input_value")
    y = calc(x_element.text)
    Otvet = browser.find_element_by_id("answer")
    Otvet.send_keys(y)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла