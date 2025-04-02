from django.db import models

# Create your models here.
class Course(models.Model):
    id_number = models.CharField(max_length=8)
    class_name = models.CharField(max_length=10)
    date = models.CharField(max_length = 3)
    time = models.TimeField()

    def __str__(self):
        return f"Course: {self.class_name}"