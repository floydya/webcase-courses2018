from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import *

admin.site.register(Article)


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, MyAdmin)
