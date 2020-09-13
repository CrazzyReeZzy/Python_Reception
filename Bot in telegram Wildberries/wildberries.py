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
        if ( data_category == category ):
            lastkey = config["Wildberries"]["lastkey"]  # обращаемся как к обычному словарю!
            lastkey = int(lastkey)# lastkey - приведенный int
        else:
            lastkey = 0
        return lastkey

    def new_clothes(self, url, lastkey):
        r = requests.get(url)
        html = BS(r.content, 'html.parser')
        new = []
        items = html.select('.ref_goods_n_p') # вар -- cat
        for i in items:
                key = self.parse_href(i['href'])
                if (lastkey < int(key)):
                    new.append(i['href'])
        return new
    
    def parse_href(self, href):
        result = re.search(r'\d+', href)
        return result.group(0)

    
    def get_new_lastkey(self,category,new_lastkey):
        pass

    def new_lastkey(self,category,new_lastkey):
        new_config = configparser.ConfigParser()  # создаём объекта парсера
        new_config.read("data.ini")  # читаем конфиг
        if (category == new_config["Wildberries"]["category"]):
            new_config.set("Wildberries", "lastkey", new_lastkey)
