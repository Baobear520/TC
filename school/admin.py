from django.contrib import admin
from django.utils.html import format_html,urlencode
from django.urls import reverse
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    

    

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('date_enrolled','student','course')
    date_hierarchy = 'date_enrolled'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    
