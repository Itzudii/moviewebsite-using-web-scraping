import requests as req
from bs4 import BeautifulSoup as bs



class Kat:
    def __init__(self,base):
        self.base = base
        # self.base = 'https://katmoviehd.blue/'

    def search(self,name):
        newName = name.replace(' ','+')
        response = req.get(self.base+f'?s={newName}')
        soup = bs(response.text,'html.parser')
        block  =soup.find_all('div',class_='post-thumb')
        block = [i.find('a') for i in block]
        result = [{'link':tag['href'],'title':tag['title'],'img': tag.find('img')['src']} for tag in block]
        return result