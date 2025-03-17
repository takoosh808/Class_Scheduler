from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerializer, DetailedCourseSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(["GET"])
def courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def course_detail(request, slug):
    courses = Course.objects.all(slug=slug)
    serializer = DetailedCourseSerializer(courses)
    return Response(serializer.data)