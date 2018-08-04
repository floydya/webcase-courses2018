import os
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from unidecode import unidecode
from ckeditor.fields import RichTextField


def slugger(string):
    """
    Конвертирование строки в SLUG-подобную для генерации
    SEO-дружественных ссылок
    """
    slug = slugify(unidecode(string))
    unique_slug = slug
    num = 1
    while Article.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug


def path_and_rename(instance, filename):
    """
    Переименование загруженного файла в формат:
        название-статьи.расширение
    """
    upload_to = 'articles'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(slugger(instance.title), ext)
    return os.path.join(upload_to, filename)


class Category(models.Model):
    """
    Модель категорий сайта
    """
    slug = models.SlugField(max_length=40, editable=False, unique=True)
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Переопределение метода 'save' для правки SLUG
        """
        self.slug = slugger(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])


class Image(models.Model):
    """
    Модель изображений для генерации "галереи" в статье
    """
    image = models.ImageField(upload_to='gallery', verbose_name='Изображение')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='gallery', verbose_name='Статья')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image.url


class Article(models.Model):
    """
    Модель статьи
    """
    slug = models.SlugField(max_length=60, unique=True, editable=False)

    title = models.CharField(max_length=60, verbose_name='Заголовок', unique=True)
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles',
                               verbose_name='Автор', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 related_name='articles', verbose_name='Категория')
    tags = TaggableManager()
    main_image = models.ImageField(upload_to=path_and_rename, verbose_name='Главное изображение', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования статьи')

    likes = models.ManyToManyField(User, blank=True, related_name='liked', verbose_name='Понравилось', editable=False)
    dislikes = models.ManyToManyField(User, blank=True, related_name='disliked', verbose_name='Не понравилось', editable=False)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров', editable=False)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugger(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Модель комментария
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='comments', verbose_name='Автор')
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE,
                               related_name='child', verbose_name='Родительский комментарий', blank=True, null=True)
    text = models.TextField(verbose_name='Текст комментария')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования комментария')

    likes = models.ManyToManyField(User, blank=True, related_name='comment_liked', editable=False)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


@receiver(models.signals.post_delete, sender=Image)
def del_on_del(sender, instance, **kwargs):
    """
    Удаление изображения из папки /media/ при удалении
    изображения в статье
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Image)
def del_on_change(sender, instance, **kwargs):
    """
    Удаление изображения из папки /media/ при изменении
    изображения в статье
    """
    if not instance.pk:
        return False
    try:
        old_file = Image.objects.get(pk=instance.pk).file
    except Image.DoesNotExist:
        return False
    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
