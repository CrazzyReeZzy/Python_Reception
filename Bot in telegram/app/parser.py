import requests
import lxml
from bs4 import BeautifulSoup as BS

#Парсим текст - Заголовок, текст и ссылку на картинку

r = requests.get('https://stopgame.ru/articles/new')
html = BS(r.content, 'html.parser')
#Заголовок
for el in html.select('.article-summary'):
    title = el.select('.caption > a')
    print(title[0].text)
#Текст
# Идея как воровать текст
# 1. Надо спарсить ссылку на статью
# 2. Надо ее почистить
# 3. C чистой ссылкой, создаем соединение и парсим тескт.
#Ссылка на картинку - Все картинки и не обработанные
list_link = [] 
for el in html.select('.article-summary'):
    link = el.select('.image')
    list_link.append(link)
    print(link)
print(list_link[1])
#Скачиваем картинку
p = requests.get('https://images.stopgame.ru/articles/2020/08/31/c413x234/wAlIEXL377PeKGy82074UQ/1Migmop.jpg')
out = open("img\img.jpg", "wb")
out.write(p.content)
out.close()

# Функция обрезки строки
def link_format():
    str_link = '[<div class="image lazy" data-src="https://images.stopgame.ru/articles/2020/08/31/c413x234/WshDUnjizD_w8Bu6OPwUng/Sd2RAG-fH.jpg"></div>]'
    str_search = "data-src" # Под строка которую буду искать
    str_link.find(str_search) # Номер символа начала str_search


link_format()