from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(AbstractUser):
    first_name = models.CharField(max_length = 100, blank = False, null = False)
    last_name = models.CharField(max_length = 100, blank = False, null = False)
    id_number = models.CharField(max_length = 8,blank = False, null = False, primary_key = True)

    def __str__(self):
        return self.username