from django.db import models

# Create your models here.
class Course(models.Model):
    class_name = models.CharField(max_length=10)
    id_number = models.CharField(max_length=8)
    IsLab = models.BooleanField(default=False)
    Section_Number = models.IntegerField(default=1)
    Instructor = models.CharField(max_length=20, default='To Be Assigned')
    Date = models.CharField(max_length = 3)
    Time = models.CharField(max_length=4)
    Location = models.CharField(max_length=10, default='To Be Assigned')
    Enrollment_max = models.IntegerField(default=100)
    Enrollment = models.IntegerField(default=0)

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