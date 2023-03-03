from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db.models import Q, Count, OuterRef, Subquery, Value, F, Exists
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import *
# Register your models here.


class StudentInline(admin.TabularInline):
    model = Enrollment
    min_num = 1
    max_num = 2
    extra = 0
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_enrolled')
    inlines = [StudentInline]
    search_fields = ('first_name','last_name')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

    @admin.display(ordering='is_enrolled',boolean=True)
    def is_enrolled(self, student):
        return student.is_enrolled

    
    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            is_enrolled=Exists(
            Enrollment.objects.filter(
            student=OuterRef('pk')).filter(lessons__gt=0))
            
        )
                            
        


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    exclude = ('lessons',)
    autocomplete_fields = ('student',)
    list_display = ('date_enrolled', 'student',
                    'course', 'money_paid', 'lessons')
    date_hierarchy = 'date_enrolled'
    list_filter = ('student','course')
    list_editable = ('lessons', 'money_paid')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_of_current_enrollments')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


    @admin.display(ordering='number_of_current_enrollments')
    def number_of_current_enrollments(self, course):
        return course.number_of_current_enrollments

    def get_queryset(self, request):
        num = Count(
            'enrollment',
            filter=Q(enrollment__lessons__gte=1)
        )
        return super().get_queryset(request).annotate(
            number_of_current_enrollments=num)


class LevelInline(admin.TabularInline):
    model = Course
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':30})},
    }
    min_num = 1
    extra = 0
    
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [LevelInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }