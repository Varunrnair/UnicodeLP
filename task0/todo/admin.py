from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email','first_name')
    
    list_display = ('email','username','first_name','is_active','is_staff','profile_pic')

admin.site.register(List)
admin.site.register(User, UserAdminConfig)
