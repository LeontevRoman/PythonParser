import requests as r
from bs4 import BeautifulSoup as bs

url = 'https://skillbox.ru/course/sql-analysis/'
adress = r.get(url)
html_soup = bs(adress.text, 'lxml')

class Parser():
    default_p = ''
    default_h1 = ''
    default_h2 = ''

    def __init__(self, p=default_p, h1=default_h1, h2=default_h2) :
        self.p = p
        self.h1 = h1
        self.h2 = h2

    def find_h1(self, html_h1):
        self.h1 = html_h1.findAll('h1')
        print(f'Заголовки h1')
        for h1 in self.h1:
            print(h1.text)


    def find_h2(self, html_h2):
        self.h2 = html_h2.findAll('h2')
        print(f'Заголовки h2')
        for h2 in self.h2:
            print(h2.text)


    def find_p(self, html_p):
        self.p = html_p.findAll('p')
        print(f'Абзацы p')
        for p in self.p:
            print(p.text, sep='n/')

if __name__ == '__main__':

    parser = Parser()

    parser.find_h1(html_soup)
    parser.find_h2(html_soup)
    parser.find_p(html_soup)


