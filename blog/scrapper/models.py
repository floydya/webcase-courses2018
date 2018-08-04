from django.db import models


class ParsedArticle(models.Model):
    """
    Модель статей для парсинга с сайтов, используется как промежуточная
    между этим сайтом и тем, который парсится
    """
    title = models.CharField(max_length=120, unique=True)
    body = models.TextField()
    image = models.URLField()
    tags = models.CharField(max_length=500)
