from django.urls import path

from article import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('create/', views.ArticleCreate.as_view(), name='article-create'),
    path('article/<slug>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('article/<slug>/update/', views.ArticleUpdate.as_view(), name='article-update'),
    path('article/<slug>/delete/', views.ArticleDelete.as_view(), name='article-delete'),
    path('api/', views.ApiRoot.as_view(), name='api-root'),
    path('api/categories/', views.CategoryListAPI.as_view(), name='category-list-api'),
    path('api/category/<pk>/', views.CategoryDetailAPI.as_view(), name='category-detail-api'),
    path('api/articles/', views.ArticleListAPI.as_view(), name='article-list-api'),
    path('api/article/<pk>/', views.ArticleDetailAPI.as_view(), name='article-detail-api')
]
