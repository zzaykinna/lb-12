from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://food.ru/kalkulyator-kalorii')

buttonAge=browser.find_element(By.NAME, "age")
buttonAge.send_keys('18')

buttonH=browser.find_element(By.NAME, "height")
buttonH.send_keys('162')

buttonW=browser.find_element(By.NAME, 'weight')
buttonW.send_keys('55')

button=browser.find_element(by=By.CSS_SELECTOR, value='._18Bed')

button.click()

try:
    assert 'Калькулятор расчёта калорий' in browser.title
    print('Все отлично')
except Exception as err:
    print('Что-то не так(')

try:
    assert 'результат' in browser.page_source
    print('Все отлично')
except Exception as err:
    print('Что-то не так(')

browser.close()