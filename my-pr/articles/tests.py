from django.contrib.auth.models import User
from django.test import TestCase
from .models import Article


class ArticleTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Инициализация данных для тестов
        """
        user = User.objects.create(username='user1', email='myemail@mail.ru')
        user.set_password("password")
        Article.objects.create(title='Title',
                               short_description='Short description',
                               body='Article body',
                               created_by=user
                               )

    def test_title_label(self):
        """
        Тестирование лейбла заголовка
        """
        article = Article.objects.get(id=1)
        field_title = article._meta.get_field('title').verbose_name
        self.assertEquals(field_title, 'title')

    def test_short_desc_label(self):
        """
        Тестирование лейбла описания
        """
        article = Article.objects.get(id=1)
        field_short_description = article._meta.get_field('short_description').verbose_name
        self.assertEquals(field_short_description, 'short description')

    def test_body_label(self):
        """
        Тестирование лейбла тела
        """
        article = Article.objects.get(id=1)
        field_body = article._meta.get_field('body').verbose_name
        self.assertEquals(field_body, 'body')

    def test_created_by_label(self):
        """
        Тестирование лейбла создателя
        """
        article = Article.objects.get(id=1)
        field_created_by = article._meta.get_field('created_by').verbose_name
        self.assertEquals(field_created_by, 'created by')

    def test_get_url(self):
        """
        Тестирование функции получения ссылки на статью
        """
        article = Article.objects.get(id=1)
        self.assertEquals(article.get_url(), '/article/1/')
