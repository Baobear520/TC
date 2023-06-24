from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    STUDENT = 'Student'
    ADMIN = 'Admin'
    STAFF = 'Staff'

    STATUS_CHOICES = [
        (STUDENT,'Student'),
        (ADMIN,'Admin'),
        (STAFF,'Staff'),
    ]
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='Student')
    

    
