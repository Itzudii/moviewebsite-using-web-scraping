import requests as req
from bs4 import BeautifulSoup as bs

class MovieNation:
    def __init__(self,base):
        # self.base = 'https://moviesnation.onl/'
        self.base = base

    def search(self,name):
        newName = name.replace(' ','+')
        response = req.get(self.base+f'?s={newName}')
        soup = bs(response.text,'html.parser')
        article = soup.find_all('article',class_ = 'jeg_post')
        a = [tag.find('a') for tag in article]
        result = []
        for i in a:
            img = i.find('img')
            d = {
                'link':i['href'],
                'img':img['data-src'],
                'title':img['alt']
            }
            result.append(d)
        return result
                
