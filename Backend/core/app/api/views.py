from rest_framework.views import APIView
from ..models import Course,Student, Cart, CartItem
from .serializers import CourseSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import pandas as pd
import os,json, logging

class CourseViewSet(APIView):
    def get(self, request):
        excel_path = os.path.join(os.path.dirname(__file__), 'courses.xlsx')
        df = pd.read_excel(excel_path)

        # course_data = df.to_dict(orient='records')
        # return Response(course_data)

        imported_courses = []
        df = df.map(lambda x: x.strip() if isinstance(x,str) else x)
        for _, row in df.iterrows():
            print(f"Checking row: {row.to_dict()}")
            course_id = row['id_number']
            if len(str(course_id)) > 10:
                print(f"id_number too long: {course_id} ({len(str(course_id))})")
            course, created = Course.objects.get_or_create(
                id_number=row['id_number'],  # Use this as unique ID or change as needed
                defaults={
                    'class_name': row['class_name'],
                    'Section_Number': row['Section_Number'],
                    'Instructor': row.get('Instructor', 'TBA'),
                    'Date': row.get('Date', ''),
                    'Time': row.get('Time', ''),
                    'Location': row.get('Location', 'TBA'),
                    'Enrollment_max': row.get('Enrollment_max', 100),
                    'Enrollment': row.get('Enrollment', 0),
                    'IsLab': row.get('IsLab', False)
                }
            )
            imported_courses.append({
                'class_name': course.class_name,
                'id_number': course.id_number,
                'Section_Number': course.Section_Number,
                    'Instructor': course.Instructor,
                    'Date': course.Date,
                    'Time': course.Time,
                    'Location': course.Location,
                    'Enrollment_max': course.Enrollment_max,
                    'Enrollment': course.Enrollment,
                    'IsLab': course.IsLab
            })

        return Response({
            'message': 'Courses imported successfully.',
            'imported': imported_courses
        })
    
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
            # print(Student._meta.db_table)
            student = Student.objects.get(id_number=id)
            if student.password == password:
                return JsonResponse({'token':f"{id}"})
            else:
                return JsonResponse({'error':'Invalid password'},status=400)
        except Student.DoesNotExist:
            return JsonResponse({'error':'Student does not exist!'},status=404)
    return JsonResponse({'error':'Invalid response'},status=400)

@csrf_exempt
def UserView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        # print(Student.objects.filter(id_number=id))
        # print(Student.objects.all())
        # print(f"ID:{id}")
        try:
            student = Student.objects.get(id_number=id)
            return JsonResponse({'user':f"{student.first_name} {student.last_name}"})
        except Student.DoesNotExist:
            logging.warning(f"Error retrieving student: {id}")
            return JsonResponse({'error':f'Could not retrieve student: {id}'})

@api_view(['POST'])
def add_to_cart(request):
    try:
        student_id = request.data['student_id']
        course_id = request.data['course_id']

        student = Student.objects.get(id_number=student_id)
        course = Course.objects.get(id_number=course_id)

        # Create or get a cart
        cart, _ = Cart.objects.get_or_create(student=student)

        # Check if this course is already in the cart
        item, created = CartItem.objects.get_or_create(cart=cart, course=course)
        if not created:
            item.quantity += 1
            item.save()

        return Response({"message": "Course added to cart!"}, status=status.HTTP_200_OK)

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def view_cart(request, student_id):
    try:
        student = Student.objects.get(id_number=student_id)
        cart = Cart.objects.get(student=student)
        items = CartItem.objects.filter(cart=cart).select_related('course')

        data = [
            {
                'course_name': item.course.class_name,
                'id_number': item.course.id_number,
                'quantity': item.quantity,
            }
            for item in items
        ]
        return JsonResponse({'cart': data})

    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)
    except Cart.DoesNotExist:
        return JsonResponse({'cart': []})

@api_view(['POST'])
def enroll_courses(request):
    print("Received data:", request.data)
    student_id = request.data.get('student_id')
    if not student_id:
        return JsonResponse({'error': 'student_id missing'}, status=400)

    try:
        student = Student.objects.get(id_number=student_id)
        cart = Cart.objects.get(student=student)
        cart_items = CartItem.objects.filter(cart=cart)

        enrolled = []

        for item in cart_items:
            course = item.course

            if course.Enrollment < course.Enrollment_max:
                student.enrolled_courses.add(course)
                course.Enrollment += 1
                course.save()
                enrolled.append(course.class_name)

        # Clear cart after enrolling
        cart_items.delete()

        return JsonResponse({'message': 'Enrollment successful', 'enrolled_courses': enrolled})

    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@api_view(['GET'])
def view_enrolled_courses(request, student_id):
    try:
        student = Student.objects.get(id_number=student_id)
        courses = student.enrolled_courses.all()

        data = [
            {
                "class_name": c.class_name,
                "id_number": c.id_number,
                "instructor": c.Instructor,
                "time": c.Time,
                "date": c.Date,
                "location": c.Location
            }
            for c in courses
        ]

        return Response({"enrolled_courses": data})

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=404)