from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json

url = "https://news.bitcoin.com/"

class Topic:

    objects = []

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.body = kwargs.get('body', None)
        self.image = kwargs.get('image', None)
        self.tags = kwargs.get('tags', None)
        Topic.objects.append(self)
        print('{} topic created: Topic.objects[{}]'.format(len(Topic.objects), len(Topic.objects)-1))

    @classmethod
    def save_all(cls):
        with open('z.json', "w+") as file:
            file.write(json.dumps([vars(ob) for ob in Topic.objects]))

    def save(self):
        dictionary = vars(self)
        json_return = json.dumps(dictionary, sort_keys=True, indent=4)
        with open('a.json', "a") as file:
            file.write(json_return)

get_urls = lambda soup: [link.find('a').get('href') for link in 
                         soup.find_all('h3', class_='entry-title')]

def open_url(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf8')
        return webpage
    except Exception as err:
        return None

for i in range(1, 2):

    soup = BeautifulSoup(open_url(url+"page/"+str(i)+"/"), features='html.parser')

    links = get_urls(soup)

    for link in links:
        link_soup = BeautifulSoup(open_url(link), features='html.parser')
        title = link_soup.find('h1', class_="entry-title").get_text()
        body = " ".join([text.get_text() for text in link_soup.find_all('p')])
        image = link_soup.find('img', class_='entry-thumb').get('src')
        tags = [tag.get_text() for tag in link_soup.find('ul', 
            class_='td-tags').children if tag.get_text() != 'TAGS']
        Topic(title=title, body=body, image=image, tags=tags)
