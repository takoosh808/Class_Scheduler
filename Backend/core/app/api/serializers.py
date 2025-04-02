from .. models import Course
from rest_framework.serializers import ModelSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id_number', 'class_name', 'date', 'time')
        