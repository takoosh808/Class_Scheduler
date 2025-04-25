from django.db import models

# Create your models here.
class Course(models.Model):
    class_name = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20, primary_key=True)
    IsLab = models.BooleanField(default=False)
    Section_Number = models.IntegerField(default=1)
    Instructor = models.CharField(max_length=30, default='To Be Assigned')
    Date = models.CharField(max_length = 3)
    Time = models.CharField(max_length=4)
    Location = models.CharField(max_length=30, default='To Be Assigned')
    Enrollment_max = models.IntegerField(default=100)
    Enrollment = models.IntegerField(default=0)

    def __str__(self):
        return self.class_name
    
    
class Student(models.Model):
    id_number = models.CharField(max_length=8,default = "-1", primary_key=True, unique=True)
    first_name = models.CharField(max_length=50, default="Jane")
    last_name = models.CharField(max_length=50, default="Smith")
    password = models.CharField(max_length = 50, default="abc123")
    enrolled_courses = models.ManyToManyField(Course, blank=True, related_name='enrolled_students')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"  
    class Meta:
        db_table = 'app_student'
    
class Cart(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,to_field='id_number',on_delete=models.CASCADE,db_column='course_id')
    quantity = models.IntegerField(default=1)