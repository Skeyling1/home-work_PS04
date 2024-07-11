# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# # 1. Спрашивать у пользователя первоначальный запрос.
# # 2. Переходить по первоначальному запросу в Википедии.
# # 3. Предлагать пользователю три варианта действий:
# # листать параграфы текущей статьи;
# # перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# # - листать параграфы статьи;
# # - перейти на одну из внутренних статей.
# # выйти из программы.

from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
#import time

browser = webdriver.Firefox()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")
time.sleep(3)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
browser.refresh()


browser.quit()
