from django import forms


class ArticleSearchForm(forms.Form):
    """
    Форма поиска на страницах сайта
    """
    search_text = forms.CharField(
        required=False,
        label='Search...',
        widget=forms.TextInput(attrs={'placeholder': 'Поиск...'})
    )
