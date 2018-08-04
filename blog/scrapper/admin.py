from django.contrib import admin
from django.contrib.auth.models import User

from article.models import Article, Category
from scrapper.models import ParsedArticle


def save_articles(modeladmin, request, queryset):
    """
    Копирует выделенные записи из модели ParsedArticle в Article и удаляет их с первой.
    """
    for article in queryset.all():
        new_article = Article()
        new_article.title = article.title
        new_article.body = article.body

        new_article.main_image = article.image

        new_article.author = User.objects.get(pk=1)
        new_article.category = Category.objects.first()
        new_article.save()
        new_article.tags.add(*[t.strip().lower() for t in article.tags.split(',') if t.strip()])
        new_article.save()
        article.delete()
    save_articles.short_description = "Сохранить статью в БД"


class ParsedArticleAdmin(admin.ModelAdmin):
    """
    Добавление действия над списком парснутых статей, добавление кнопки "Импорт" сверху.
    """
    list_display = ['title']
    ordering = ['id']
    actions = [save_articles]
    change_list_template = 'admin/scrapper/parsedarticle/change_list.html'


admin.site.register(ParsedArticle, ParsedArticleAdmin)
