from django.contrib.auth.models import User
from rest_framework import serializers

from article.models import Article, Category, Image


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор категории с генерацией ссылок
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='category-detail-api',
        lookup_field='pk',
    )
    articles = serializers.HyperlinkedIdentityField(
        view_name='article-detail-api',
        lookup_field='pk', many=True,
    )

    class Meta:
        model = Category
        fields = ('url', 'name', 'articles')


class GallerySerializer(serializers.ModelSerializer):
    """
    Сериализатор изображений галереи
    """
    class Meta:
        model = Image
        fields = ('image', )


class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериализатор статьи
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='article-detail-api',
        lookup_field='pk',
    )
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    gallery = GallerySerializer(many=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('url', 'title', 'body', 'author', 'category', 'created_at', 'main_image', 'gallery', 'likes', 'views')

    def get_likes(self, obj):
        """
        Получение количества лайков
        """
        return obj.likes.count()