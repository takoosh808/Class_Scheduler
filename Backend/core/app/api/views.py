from rest_framework.views import APIView
from ..models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response

class CourseViewSet(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)