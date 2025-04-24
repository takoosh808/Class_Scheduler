from rest_framework.views import APIView
from ..models import Course,Student
from .serializers import CourseSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
import pandas as pd
import os,json

class CourseViewSet(APIView):
    def get(self, request):
        excel_path = os.path.join(os.path.dirname(__file__), 'courses.xlsx')
        df = pd.read_excel(excel_path)

        course_data = df.to_dict(orient='records')
        return Response(course_data)
    
@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        password = data.get('password')
        print(f"ID:{id}, Pass:{password}")
        print(Student.objects.filter(id_number=id))

        try:
            # Student.objects.create(id_number='12345678',first_name = 'Parteek',last_name='Kumar',password='1234')
            # print(Student.objects.all())
            student = Student.objects.get(id_number=id)
            if student.password == password:
                return JsonResponse({'token':'abc123'})
            else:
                return JsonResponse({'error':'Invalid password'},status=400)
        except Student.DoesNotExist:
            return JsonResponse({'error':'Student does not exist!'},status=404)
    return JsonResponse({'error':'Invalid response'},status=400)
