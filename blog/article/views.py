import json

from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from article.models import Article, Comment, Image, Category
from article.serializers import ArticleSerializer, CategorySerializer


class ArticleList(ListView):
    """
    Представление списка статей с пагинацией(10 шт/стр),
    фильтром по категории
    """
    model = Article
    paginate_by = 10

    def get_queryset(self):
        if 'q' in self.request.GET:
            objects = Article.objects.filter(
                Q(title__icontains=self.request.GET['q']) |
                Q(body__icontains=self.request.GET['q']) |
                Q(category__name__icontains=self.request.GET['q'])
            )
        elif 'category' in self.request.GET:
            objects = Article.objects.filter(category__slug=self.request.GET['category'])
        elif 'tag' in self.request.GET:
            objects = Article.objects.filter(tags__name=self.request.GET['tag'])
        else:
            objects = Article.objects.get_queryset()
        if self.request.GET.get('order') in ('id', 'likes'):
            objects = objects.order_by(self.request.GET['order']).reverse()
        else:
            objects = objects.order_by('id').reverse()
        return objects


class ArticleDetail(DetailView):
    model = Article
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=context['object']).filter(parent=None).order_by('-created_at')
        # Счетчик посещений страницы
        Article.objects.filter(slug=self.kwargs['slug']).update(views=F('views') + 1)
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if 'type' in self.request.POST:
            if self.request.POST['type'] == 'article-like':
                article = Article.objects.get(pk=self.request.POST['like'])
                if self.request.user not in article.likes.all():
                    article.likes.add(self.request.user)
                    message = 'ADD'
                else:
                    article.likes.remove(self.request.user)
                    message = 'DEL'
                context = {'likes': article.likes.count(), 'message': message}
                return HttpResponse(json.dumps(context), content_type='application/json')
            elif self.request.POST['type'] == 'add_comment':
                article = Article.objects.get(slug=self.kwargs['slug'])
                comment = Comment.objects.create(article=article, author=self.request.user, text=self.request.POST['comment'])
                if self.request.POST.get('parent'):
                    comment.parent = Comment.objects.get(pk=self.request.POST['parent'])
                    comment.save()
                return super().get(request, *args, **kwargs)


class ArticleCreate(CreateView):
    model = Article
    fields = ('title', 'body', 'category', 'tags', 'main_image',)

    def form_valid(self, form):
        new_object = form.save()
        new_object.author = self.request.user
        new_object.save()
        for item in self.request.FILES.getlist('gallery'):
            print(item)
            Image.objects.create(image=item, article=new_object)
        return redirect('article-detail', slug=new_object.slug)


class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title', 'body', 'category', 'tags', 'main_image',)
    slug_field = 'slug'

    def form_valid(self, form):
        new_object = form.save()
        for item in self.request.FILES.getlist('gallery'):
            print(item)
            Image.objects.create(image=item, article=new_object)
        return redirect('article-detail', slug=new_object.slug)


class ArticleDelete(DeleteView):
    model = Article
    slug_field = 'slug'

"""
API Views
"""


class CategoryListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list-api'


class CategoryDetailAPI(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail-api'


class ArticleListAPI(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    name = 'article-list-api'


class ArticleDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    name = 'article-detail-api'


class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'categories': reverse(CategoryListAPI.name, request=request),
            'articles': reverse(ArticleListAPI.name, request=request),
        })