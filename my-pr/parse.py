import json
import urllib.request, urllib.parse
from articles.models import *
from django.contrib.auth.models import User


API_KEY = "315cf9763d8b47b9bee6eaa4e52e31e5"
search = 'iphone'
dictionary = {'q': search, 'sortBy': 'publishedAt', 'apiKey': API_KEY}
content = urllib.parse.urlencode(dictionary, encoding='utf-8')
response = urllib.request.urlopen("http://newsapi.org/v2/everything?" + content).read().decode('utf-8')
result = json.loads(response)
if result.get('status') == "ok":
    user = User.objects.filter(pk=1)[0]
    for article in result.get('articles'):
        dot = article.get('description').find('.')
        a = Article.objects.create(title=article.get('title'),
                               short_description=article.get('description')[0:dot+1],
                               body=article.get('description'),
                               created_by=user
                               )
        a.category.add(5)
        a.image = article.get('urlToImage')
        a.save()