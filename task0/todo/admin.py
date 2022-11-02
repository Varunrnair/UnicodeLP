from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email','user_name','first_name')
    ordering = ('first-name')
    list_display = ('email','user_name','first_name','is_active','is_staff')

admin.site.register(List)
admin.site.register(User, UserAdminConfig)
