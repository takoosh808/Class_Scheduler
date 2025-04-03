from django.urls import path
from rest_framework.routers import DefaultRouter
from . views import CourseViewSet

course_router = DefaultRouter()
course_router.register(r'courses', CourseViewSet)
