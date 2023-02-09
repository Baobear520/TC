from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    date_registered = models.DateField(auto_created=True)
    
class Level(models.Model):
    title = models.TextField(max_length=255)

class Course(models.Model):
    title = models.TextField(max_length=255)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    number_of_classes = models.IntegerField()
    price = models.DecimalField('tuition_fee',max_digits=6,decimal_places=2)
class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_created=True)
    course = models.ForeignKey(Course,on_delete=models.RESTRICT)

