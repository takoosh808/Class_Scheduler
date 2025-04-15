from rest_framework.views import APIView
from ..models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
import pandas as pd
import os

class CourseViewSet(APIView):
    def get(self, request):
        excel_path = os.path.join(os.path.dirname(__file__), 'courses.xlsx')
        df = pd.read_excel(excel_path)

        course_data = df.to_dict(orient='records')
        return Response(course_data)