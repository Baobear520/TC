import datetime
from django.contrib import admin
from django.db import models
from django.utils.html import format_html
# Create your models here.
class Student(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    date_registered = models.DateField(auto_created=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


    @admin.display(boolean=True)
    def registered_this_year(self):
        now = datetime.date.today()
        return now.year == self.date_registered.year

    class Meta:
        ordering = ['last_name']


class Level(models.Model):
    title = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title
class Course(models.Model):
    title = models.TextField(max_length=255)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    number_of_classes = models.IntegerField()
    price = models.DecimalField('tuition_fee',max_digits=9,decimal_places=2)

    def __str__(self) -> str:
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_created=True)
    course = models.ForeignKey(Course,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.student