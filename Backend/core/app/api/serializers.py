from .. models import Course, Student
from rest_framework.serializers import ModelSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        