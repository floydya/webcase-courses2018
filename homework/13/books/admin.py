from django.contrib import admin
from .models import Author, Book, BookInstance

admin.site.register(Book)
admin.site.register(BookInstance)

@admin.register(Author)
class AuthorView(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
