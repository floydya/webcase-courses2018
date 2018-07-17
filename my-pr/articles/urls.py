from django.conf.urls import url
from articles.views import ArticleView, ArticlesView

urlpatterns = [
    url(r'^$', ArticlesView.as_view(), name="articles"),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view(), name="article"),
]
