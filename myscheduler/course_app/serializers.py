from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id_number", "name", "slug", "image", "category"]

class DetailedCourseSerializer(serializers.ModelSerializer):
    prerequisites=serializers.SerializerMethodField()
    class Meta:
        fileds = ["id_number", "name", "slug", "image", "category", "prerequisites"]

        def getPrerequisites(self, course):
            courses = Course.objects.filter(category=course.category).exclude(id_number=course.id_number)
            serializer=CourseSerializer(courses, many=True)
            return serializer.data