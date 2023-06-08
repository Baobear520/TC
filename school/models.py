from typing import Any
from django.conf import settings
from django.forms import ModelForm
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.decorators import method_decorator
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models



# Create your models here.
class Student(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    photo = models.ImageField('Upload photo',upload_to='images',null=True,blank=True) 
    
    A = "a"
    B = "b"
    C = "c"
    NE = 'Not enrolled'
    GRADE_CHOICES = [
        (A,"a"),(B,"b"),(C,"c"),
        (NE,'Not enrolled')
    ]
    grade = models.CharField(max_length=15,choices=GRADE_CHOICES,default=NE)


    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    @property
    def grade_repr(self):
        if self.grade == 'Not enrolled':
            return self.grade
        enrollments = self.enrollments.filter(lessons__gt=0)  # Access all active enrollments related to the student
        for enrollment in enrollments:
            if enrollment:
                return f"{enrollment.course}{self.grade}"
            
    
    def display_grade(self):
        return self.grade_repr
    display_grade.short_description = 'Class'

    def show_image(self):
        if self.photo:
            return mark_safe(f'<img src = "{self.photo.url}" width = "300"/>')
        return '-'
    show_image.short_description = 'Photo preview'
    
    class Meta:
        ordering = ['user__last_name']
        unique_together = [['user','id']]
    

class Relative(models.Model):
    student = models.ManyToManyField(Student)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    status = models.CharField(max_length=31)
    phone_number1 = models.CharField(max_length=20,unique=True)
    phone_number2 = models.CharField(max_length=15,blank=True,null=True)
    
    class Meta:
        ordering = ['last_name']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Level(models.Model):
    STARTER = 'S'
    ELEMENTARY = 'E'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'
    
    TITLE_CHOICES = [
        (STARTER, "Starter"),
        (ELEMENTARY, "Elementary"),
        (INTERMEDIATE, "Intermediate"),
        (ADVANCED, "Advanced"),
    ]
    title = models.CharField(
        max_length=15,
        choices=TITLE_CHOICES,
        unique=True)
    description = models.TextField(max_length=611,null=True,blank=True)


    def __str__(self) -> str:
        return self.title
    
class Course(models.Model):
    STARTER_1 = "S1"
    STARTER_2 = "S2"
    STARTER_3 = "S3"
    ELEMENTARY_1 = "E1"
    ELEMENTARY_2 = "E2"
    ELEMENTARY_3 = "E3"
    INTERMEDIATE_1 = 'I1'
    INTERMEDIATE_2 = 'I2'
    INTERMEDIATE_3 = 'I3'
    ADVANCED_1 = 'A1'
    ADVANCED_2 = 'A2'
    ADVANCED_3 = 'A3'
    COURSE_CHOICES = [
        (STARTER_1, "Starter 1"),
        (STARTER_2, "Starter 2"),
        (STARTER_3, "Starter 3"),
        (ELEMENTARY_1,"Elementary 1"),
        (ELEMENTARY_2,"Elementary 2"),
        (ELEMENTARY_3,"Elementary 3"),
        (INTERMEDIATE_1,"Intermediate 1"),
        (INTERMEDIATE_2,"Intermediate 2"),
        (INTERMEDIATE_3,"Intermediate 3"),
        (ADVANCED_1,"Advanced 1"),
        (ADVANCED_2,"Advanced 2"),
        (ADVANCED_3,"Advanced 3"),
    ]
    title = models.CharField(
        max_length=15,
        choices=COURSE_CHOICES,
        unique=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,related_name='available_courses')
    description = models.TextField(max_length=611,null=True,blank=True)
    number_of_classes = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField('tuition fee',
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(0)]
        )

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title



class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT,related_name='enrollments')
    date_enrolled = models.DateField(default=timezone.now)
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    money_paid = models.DecimalField('Payment',
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(0)])
    lessons = models.PositiveIntegerField('Number of lessons left',
        blank=True)

    class Meta:
        ordering = ('date_enrolled',)

        
    def __str__(self) -> str:
        return str(self.date_enrolled)
    
    def clean(self) -> None:
        if self.lessons > self.course.number_of_classes:
            raise ValidationError('Number of lessons left cannot be greater than the number of lessons in the course.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate the instance before saving
        super().save(*args, **kwargs)