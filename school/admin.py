from django.contrib import admin
from django.db.models import Q, Count, OuterRef, Subquery, Value, F, Exists
from django.forms import TextInput, Textarea
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import *
# Register your models here.


class StudentInline(admin.TabularInline):
    model = Enrollment
    min_num = 1
    extra = 0
    actions = []
    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_enrolled')
    inlines = [StudentInline]
    search_fields = ('first_name','last_name')
    readonly_fields = ('show_image',)
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

class EnrollmentLessonsLeftFilter(admin.SimpleListFilter):
    title = 'lessons left'
    parameter_name = 'lessons left'

    def lookups(self,request,model_admin):
        return (
            ('=0','Finished course'),
            ('0< and <10','Low'),
            ('10<= and <=20', 'OK'),
            ('>20','Plenty'),
            ('>0','Currently studying')
        )
    def queryset(self, request,queryset):
        if self.value() == '=0':
            return queryset.filter(lessons=0)
        elif self.value() == '0< and <10':
            return queryset.filter(Q(lessons__gt=0) & Q(lessons__lt=10))
        elif self.value() == '10<= and <=20':
            return queryset.filter(Q(lessons__lte=20) & Q(lessons__gte=10))
        elif self.value() == '>20':
            return queryset.filter(lessons__gt=20)
        elif self.value() == '>0':
            return queryset.filter(lessons__gt=0)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    autocomplete_fields = ('student',)
    list_display = ('date_enrolled', 'student',
                    'course', 'money_paid','lessons')
    ordering = ('-lessons',)
    date_hierarchy = 'date_enrolled'
    list_filter = ('student','course',EnrollmentLessonsLeftFilter)
    list_editable = ('lessons', 'money_paid')
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','number_of_current_enrollments')
    ordering = ('-number_of_classes','-level')
    

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

    def formfield_for_dbfield(self, db_field, request,**kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'title':
            field.widget.attrs = {'size':'20',}
        if db_field.name == 'description':
            field.widget.attrs = {
                'rows':4, 
                'cols':80
            }
        return field

class LevelInline(admin.TabularInline):

    model = Course
    exclude = ('description',)
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
    
    def formfield_for_dbfield(self, db_field, request,**kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'title':
            field.widget.attrs = {
                'size':'20'}
        if db_field.name == 'description':
            field.widget.attrs = {
                'rows':4, 
                'cols':80
            }
        return field