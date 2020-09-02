import requests
import lxml
from bs4 import BeautifulSoup as BS

# Функция обрезки строки-ссылки
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
title_article = []
for el in html.select('.article-summary'):
    title = el.select('.caption > a')
    title_article.append(title[0].text)
print(title_article)

#Ссылка на картинку
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
while n != len(list_link_clear)-1:
    n = n + 1
    p = requests.get(list_link_clear[n])
    out = open("img\img"+ str(n) +".jpg", "wb")
    out.write(p.content)
    out.close()

#Текст
# 1. Получаем ссылки
text_article = []
text_article_link = []
text_article_link_clear = []
for el in html.select('.article-summary'):
    text_link = el.select('a')
    text_link = str(text_link)
    text_link = text_link[0:text_link.find(">")]
    text_article_link.append(text_link) 
n = 0
while n!=len(text_article_link):
    text_article_link_clear.append(str(link_format(str(text_article_link[n]),"href=")))
    n = n + 1
print(text_article_link_clear)
# 2. Парсим
n = 0
while n!=len(text_article_link_clear)-1:
    n = n + 1
    r = requests.get('https://stopgame.ru' + str(text_article_link_clear[n]) )
    html = BS(r.content, 'html.parser')
    for el in html.select('.article article-show'):
        text = el.select('')
        text_article.append(text)
print(text_article)