import requests as req
from bs4 import BeautifulSoup as bs
import re
from Triekit import Trie
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class filmyzilla:
    def __init__(self,base):
        self.base = base
        # self.base = 'https://www.filmyzilla15.com/'

        self.fillmyzilla = {
            'movie':{
                'tollywood':'category/South-indian-hindi-dubbed-movies.html',
                'bollywood':'category/Bollywood-full-movies.html',
                'hollywood':'category/Hollywood-movies-in-hindi-dubbed.html',
            },
            'series':{
                'bollywood':'category/18/Hindi-web-series-download/',
                'tollywood':'category/18/Hindi-web-series-download/',
                'hollywood':'category/17/Hindi-dubbed-web-series-download/',
            }
        }
    def newUrl(self,year,type_,gen):
        page = req.get(self.base+self.fillmyzilla[type_][gen], verify=False)
        soup = bs(page.text,'html.parser')
        div = soup.find_all('div',class_ = 'touch')
        for i in div:
            v = i.find('a')
            try:
               if re.search(r'\d+',v.text).group() == str(year):
                   return v['href'].replace(self.base,'').replace('default/1.html','')
            except:
                f''
    
    def search(self,name,year,type_,gen):
        fetchdata = {}
        box = Trie()
        index = 0
        url = self.base+self.fillmyzilla[type_][gen]+f'alphabet/{name[0].lower()}'
        if type_ == 'movie':
            url = self.base+self.newUrl(year,type_,gen)+f'alphabet/{name[0].lower()}'
        while True:
            index += 1
            url_r = req.get(f'{url}/{index}.html', verify=False)
            soup = bs(url_r.text,'html.parser')
            a = soup.find_all('a',class_ = 'filmyvideo')
            if a:
                for i in a:
                    img = i.find('img')
                    text = img['alt']
                    name_ = re.match(r'\w+',text.replace(' ','')).group().lower()
                    box.insert(name_)
                    fetchdata[hash(name_)] = {'link':i['href'],'title':text,'img':self.base+img['src']}
            else:
                break
        result = box.search(name.lower())
        return [fetchdata[hash(r)] for r in result]
        
