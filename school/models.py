import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    date_registered = models.DateField(auto_created=True)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class Level(models.Model):
    title = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title
class Course(models.Model):
    title = models.TextField(max_length=255)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    number_of_classes = models.IntegerField()
    price = models.DecimalField('tuition_fee',max_digits=9,decimal_places=2)
class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_created=True)
    course = models.ForeignKey(Course,on_delete=models.PROTECT)

