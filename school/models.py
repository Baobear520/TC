import datetime
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    date_registered = models.DateField(auto_created=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

    class Meta:
        ordering = ['last_name']


class Level(models.Model):
    title = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title
class Course(models.Model):
    title = models.TextField(max_length=255)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    number_of_classes = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField('tuition fee',
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(0)]
        )

    def __str__(self) -> str:
        return self.title

    

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    date_enrolled = models.DateField(auto_created=True)
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    money_paid = models.DecimalField('Payment',
        max_digits=7,
        decimal_places=1,
        validators=[MinValueValidator(0)])
    lessons = models.IntegerField('Number of lessons left',
        blank=True,
        validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return str(self.date_enrolled)

    def save(self,*args,**kwargs):
        if self.pk is None:
            self.lessons = self.course.number_of_classes
            return super().save(*args,**kwargs)
        if self.student.date_registered > self.date_enrolled:
            raise ValidationError('Enrollment date cannot be eairlier than registration date.')
        return super().save(*args,**kwargs)
    