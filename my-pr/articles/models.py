from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField
from treebeard.mp_tree import MP_Node


class Article(models.Model):
    """
    Модель статьи
    """
    title = models.CharField(max_length=40)

    short_description = models.CharField(max_length=120)

    body = HTMLField()

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ManyToManyField('Category', blank=True)

    image = models.ImageField(upload_to='static/articles/', null=True)

    likes = models.ManyToManyField(User, blank=True, related_name='users_liked')

    @property
    def comments(self):
        return Comment.objects.filter(article=self)

    def __str__(self):
        """
        Строковое представление объекта
        :return:
        'Название' [by 'Пользователь', date: 'Дата создания']
        """
        return '{0.title} [by {0.created_by}, date: {0.created_at}]'.format(self)

    def get_absolute_url(self):
        """
        Получение ссылки на статью
        :return:
        article/<id>/
        """
        return reverse('article', args=[str(self.id)])

    def like(self, user):
        self.likes.add(user)
        return True

    def unlike(self, user):
        self.likes.remove(user)
        return True

    @property
    def like_count(self):
        return len(self.likes.all())


class Category(MP_Node):
    """
    Модель категорий
    Использовано: django-treebeard
    """
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return '%s' % self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
