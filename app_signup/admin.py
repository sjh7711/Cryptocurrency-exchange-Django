from django.contrib import admin
from .models import *

# Register your models here.

class UserListAdmin(admin.ModelAdmin):
    list_display=('user_pk', 'user_id', 'user_pw', 'user_pn', 'user_em')
admin.site.register(UserList,UserListAdmin)