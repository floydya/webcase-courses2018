from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import Profile
from django.contrib.auth.models import User


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
