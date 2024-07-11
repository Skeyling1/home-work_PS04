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

user_req = input("введите запрос")

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title


#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys(user_req)
time.sleep(3)
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)


time.sleep(30)




browser.quit()
