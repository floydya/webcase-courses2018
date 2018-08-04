from django.contrib import admin

from article.models import Article, Category, Comment, Image

admin.site.register(Category)
admin.site.register(Comment)


class ImageAdminInLine(admin.StackedInline):
    """
    Добавление галереи в форму редактирования статьи
    """
    model = Image
    fk_name = 'article'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Переопределение админ модели для Article
    """
    list_display = ('title', 'author', 'category', 'views')
    list_filter = ('category', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'body', 'author', 'category', 'tags')
        }),
        ('Изображения', {
            'fields': ('main_image',)
        })
    )

    inlines = [ImageAdminInLine]

    class Media:
        js = ('/static/admin-ckeditor.js',)
