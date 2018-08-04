from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

from scrapper.models import ParsedArticle


@user_passes_test(lambda u: u.is_superuser)
def import_from_site(request):
    """
    Парсер страниц новостей, вытигивает статьи и помещает их в
    промежутночную модель ParsedArticle
    """
    url = "https://news.bitcoin.com/"

    # Вытаскивает ссылки на все статьи со страницы
    get_urls = lambda soup: [link.find('a').get('href') for link in
                             soup.find_all('h3', class_='entry-title')]

    def open_url(url):
        """
        Открывает URL и отдает всю веб-страницу текстом
        """
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read().decode('utf8')
            return webpage
        except Exception as err:
            return None

    for i in range(1, 5):

        soup = BeautifulSoup(open_url(url + "page/" + str(i) + "/"), features='html.parser')

        links = get_urls(soup)

        for link in links:
            link_soup = BeautifulSoup(open_url(link), features='html.parser')
            title = link_soup.find('h1', class_="entry-title").get_text()
            body = " ".join([text.get_text() for text in link_soup.find_all('p')])
            image = link_soup.find('img', class_='entry-thumb').get('src')
            tags = ", ".join([tag.get_text() for tag in link_soup.find('ul',
                                                                       class_='td-tags').children if
                              tag.get_text() != 'TAGS'])
            ParsedArticle.objects.create(title=title, body=body, image=image, tags=tags)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
