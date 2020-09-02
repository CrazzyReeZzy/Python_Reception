import requests
import lxml
from bs4 import BeautifulSoup as BS

# Функция обрезки строки
def link_format(str_link,str_search):
    #str_link = '[<div class="image lazy" data-src="https://images.stopgame.ru/articles/2020/08/31/c413x234/WshDUnjizD_w8Bu6OPwUng/Sd2RAG-fH.jpg"></div>]'
    #str_search = "data-src" # Под строка которую буду искать
    numer_start = str_link.find(str_search) # Номер символа начала str_search
    numer_end = len(str_link) # Длина строки
    str_link = str_link[numer_start:numer_end]
    str_link = str_link[str_link.find('"')+1:str_link.rfind('"')]
    return str_link

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
n = 0
list_link_clear = []
while n!=len(list_link):
    list_link_clear.append(str(link_format(str(list_link[n]),"data-src")))
    n = n + 1
print(list_link_clear)
#Скачиваем картинку
n = 0
while n!=len(list_link_clear):
    n = n + 1
    p = requests.get(list_link_clear[n])
    out = open("img\img"+ str(n) +".jpg", "wb")
    out.write(p.content)
    out.close()

