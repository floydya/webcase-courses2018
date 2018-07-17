from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Article, Comment


class ArticlesView(ListView):
    """
    Список всех статей, пагинация по 10 штук на страницу.
    """
    model = Article
    paginate_by = 10
    template_name = 'articles/article_list.html'
    ordering = ['-id']

    def get_queryset(self):
        if 'order' in self.request.GET:
            if self.request.GET['order'] in ('-likes', '-id'):
                self.ordering = [self.request.GET['order'], '-id']
        if 'searching' in self.request.GET:
            objects = Article.objects.filter(
                Q(title__icontains=self.request.GET['searching']) |
                Q(body__icontains=self.request.GET['searching']) |
                Q(category__name__icontains=self.request.GET['searching'])
            ).order_by(self.ordering[0])
        else:
            objects = Article.objects.get_queryset().order_by(self.ordering[0])
        return objects


class ArticleView(DetailView):
    """
    Вывод конкретной статьи на страницу.
    """
    model = Article

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if 'like' in self.request.POST:
            article = Article.objects.get(pk=self.request.POST['like'])
            if self.request.user not in article.likes.all():
                article.likes.add(self.request.user)
            else:
                article.likes.remove(self.request.user)
        if 'body' in self.request.POST:
            article = Article.objects.get(pk=self.request.POST['article'])
            comment = Comment.objects.create(article=article, author=self.request.user, body=self.request.POST['body'])
            comment.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))

    def get(self, request, *args, **kwargs):
        if 'searching' in request.GET:
            return HttpResponseRedirect('%s?%s=%s' % ('/', 'searching', request.GET['searching']))
        return super(ArticleView, self).get(request)

    def get_object(self):
        return super(ArticleView, self).get_object()
