from typing import Any, Callable, Tuple, Union
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','status','is_active','link_to_student_profile')
    list_per_page = 10
    search_fields = ('username',)
    list_filter = ('status','is_active')

    
    @admin.display
    def link_to_student_profile(self,obj):
        url = (
            reverse(f'admin:school_student_change',args=(obj.student.id,))
        )
        link_html = f'<a href="{url}">{obj.student}<a>'
        return format_html(link_html)
    link_to_student_profile.short_description = 'Profile' 
        

    

    

   