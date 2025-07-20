import requests as req
from bs4 import BeautifulSoup as bs

class Bolly:
    def __init__(self,base):
        # self.base = 'https://bollyflix.army/'
        self.base = base

    def search(self,name):
        newName = name.replace(' ','+')
        response = req.get(self.base+f'search/{newName}')
        soup = bs(response.text,'html.parser')
        post = soup.find_all('article',class_='latestPost')
        a = [i.find('a') for i in post]
        result = [{'link':info['href'],'title':info['title'],'img':info.find('img')['src']} for info in a]
        return result