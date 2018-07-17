from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from articles.models import Article


GENDER = (
    ('m', 'male'),
    ('f', 'female'),
)


class Profile(models.Model):
    """
    Расширенная модель пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    avatar = models.ImageField(upload_to='static/avatars/', default='static/avatars/tom.jpg')
    gender = models.CharField(max_length=1, choices=GENDER, default='m', blank=True)

    @property
    def full_name(self):
        return " ".join(self.first_name, self.last_name)

    @property
    def articles(self):
        """
        :return:
        Список статей, написанных пользователем
        """
        return Article.objects.filter(created_by=self.user)

    @property
    def last_articles(self):
        """
        :return:
        Список последних статей, написанных пользователем
        """
        return Article.objects.filter(created_by=self.user).order_by('-id')[:5]

    @property
    def gend(self):
        return "а" if self.gender == 'f' else ""

    def get_absolute_url(self):
        return reverse('profile', args=[self.pk])
