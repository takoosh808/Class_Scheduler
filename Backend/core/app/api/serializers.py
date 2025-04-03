from .. models import Course, Student
from rest_framework.serializers import ModelSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id_number', 'class_name', 'date', 'time')


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id_number', 'name', 'password')
        