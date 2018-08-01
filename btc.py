from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import re

url = "https://blog.btc.com/"

class Topic:

    objects = []

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.body = kwargs.get('body', None)
        self.image = kwargs.get('image', None)
        self.tags = kwargs.get('tags', None)
        Topic.objects.append(self)
        print('{} topic created: Topic.objects[{}]'.format(len(Topic.objects), len(Topic.objects)-1))

#funcs
get_urls = lambda soup: [link.get('href') for link in soup.find_all('a') if link.get('data-action') == 'open-post']

def open_url(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf8')
        return webpage
    except Exception as err:
        return None

soup = BeautifulSoup(open_url(url), features='html.parser')

links = get_urls(soup)
for link in links:
    link_soup = BeautifulSoup(open_url(link), features='html.parser')
    title = link_soup.find('h1').get_text()
    body = " ".join([text.get_text() for text in link_soup.find_all('p', class_='graf--p') if 'graf--trailing' not in text.get('class')]) 
    image = link_soup.find('img', class_='graf-image').get('src')
    tags = [tag.get_text() for tag in link_soup.find('ul', class_='tags').children]
    Topic(title=title, body=body, image=image, tags=tags)
