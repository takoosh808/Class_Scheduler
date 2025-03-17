from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(AbstractUser):
    username = models.EmailField(unique=True)
    password = models.CharField(max_length = 100, blank = False, null = False)
    
    def __str__(self):
        return self.username
