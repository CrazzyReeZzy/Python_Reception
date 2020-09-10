import re
import os.path
import requests
from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
import configparser

class Wildberries():
    host = 'https://www.wildberries.ru/'
    def __init__(self):
        pass
    
    def get_url(self,category):
        self.category = category
        if (category == 1):
            url = 'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki'
        return url

    def get_lastkey(self,category):
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read("data.ini")  # читаем конфиг
        data_category = config["Wildberries"]["category"]
        int(data_category)
        if ( data_category == category ):
            lastkey = config["Wildberries"]["lastkey"]  # обращаемся как к обычному словарю!
        else:
            lastkey = 0
        return lastkey

    def new_clothes(self, url, lastkey):
        r = requests.get(url)
        html = BS(r.content, 'html.parser')
        new = []
        items = html.select('.ref_goods_n_p')
        for i in items:
                new.append(i['href'])
        return new