from typing import Any, Callable, Tuple, Union
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','status','is_active')
    list_per_page = 10
    search_fields = ('username',)
    list_filter = ('status','is_active')


    

    

   