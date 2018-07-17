from search_views.filters import BaseFilter

class ArticleFilter(BaseFilter):
    """
    Указатель на поля, по которым ведется поиск на сайте.
    """
    search_fields = {
        'search_text': ['title', 'short_description', 'body']
    }
