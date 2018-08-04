from article.models import Category


def categories(request):
    """
    Добавление категорий в контекст всех вьюх для
    отображения выпадашки в меню
    """
    return {'categories': Category.objects.all()}
