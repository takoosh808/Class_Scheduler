from django.db import models

# Create your models here.
class Course(models.Model):
    id_number = models.CharField(max_length=8)
    class_name = models.CharField(max_length=10)
    date = models.CharField(max_length = 3)
    time = models.CharField(max_length=4)

    def __str__(self):
        return self.class_name
    
class Student(models.Model):
    id_number = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length = 30)
    shoppingCart1 = models.CharField(max_length=8)
    shoppingCart2 = models.CharField(max_length=8)
    shoppingCart3 = models.CharField(max_length=8)
    shoppingCart4 = models.CharField(max_length=8)
    shoppingCart5 = models.CharField(max_length=8)
    shoppingCart6 = models.CharField(max_length=8)
    shoppingCart7 = models.CharField(max_length=8)
    shoppingCart8 = models.CharField(max_length=8)
    shoppingCart9 = models.CharField(max_length=8)
    shoppingCart10 = models.CharField(max_length=8)

    def __str__(self):
        return self.name  