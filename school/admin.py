from django.contrib import admin
from django.db.models import Q, Count, OuterRef, Subquery, Value, F, Exists
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import *
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_enrolled')

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
    list_display = ('date_enrolled', 'student',
                    'course', 'money_paid', 'lessons')
    date_hierarchy = 'date_enrolled'
    list_filter = ('student',)
    list_editable = ('lessons', 'money_paid')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_of_current_enrollments')

    @admin.display(ordering='number_of_current_enrollments')
    def number_of_current_enrollments(self, course):
        return course.number_of_current_enrollments

    def get_queryset(self, request):
        current_year = datetime.datetime.now().year
        num = Count(
            'enrollment',
            filter=Q(enrollment__date_enrolled__year=current_year)
        )
        return super().get_queryset(request).annotate(
            number_of_current_enrollments=num)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title',)
