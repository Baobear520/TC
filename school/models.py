from django.conf import settings
from django.forms import ModelForm
from django.utils import timezone
from django.utils.html import mark_safe
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models



# Create your models here.
class Student(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    photo = models.ImageField('Upload photo',upload_to='images',null=True,blank=True) 
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    def show_image(self):
        if self.photo:
            return mark_safe(f'<img src = "{self.photo.url}" width = "300"/>')
        return '-'
    show_image.short_description = 'Photo preview'
    
    class Meta:
        ordering = ['user__last_name']

    


class Level(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=611,null=True,blank=True)
    def __str__(self) -> str:
        return self.title
    
class Course(models.Model):
    title = models.TextField(max_length=255)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    description = models.TextField(max_length=611,null=True,blank=True)
    number_of_classes = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField('tuition fee',
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(0)]
        )

    def __str__(self) -> str:
        return self.title



class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
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
    
    def save(self,*args,**kwargs):
        if self.pk is None:
            self.lessons = self.course.number_of_classes
        if self.lessons > self.course.number_of_classes:
            raise ValidationError('Number of lessons left cannot be greater than number of lessons in a course')
        return super().save(*args,**kwargs)
    
    

   
   
