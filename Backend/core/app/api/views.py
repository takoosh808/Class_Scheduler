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
        courses = Course.objects.all()
        data = [
            {
                'id_number': course.id_number,
                'class_name': course.class_name,
                'Section_Number': course.Section_Number,
                'Instructor': course.Instructor,
                'Date': course.Date,
                'Time': course.Time,
                'Location': course.Location,
                'Enrollment_max': course.Enrollment_max,
                'Enrollment': course.Enrollment,
                'IsLab': course.IsLab
            }
            for course in courses
        ]
        return Response(data)
    
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
                'date': item.course.Date,
                'time': item.course.Time,
                'location': item.course.Location,
                'instructor': item.course.Instructor,
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
    student_id = request.data.get('student_id')
    course_id = request.data.get('course_id') 

    try:
        student = Student.objects.get(id_number=student_id)
        new_course = Course.objects.get(id_number=course_id)
        
        currently_enrolled = student.enrolled_courses.all()

        # Check for direct duplicate enrollment
        if currently_enrolled.filter(id_number=new_course.id_number).exists():
            return Response({
                "message": "Already enrolled in this course."
            }, status=400)

        if student.enrolled_courses.filter(class_name=new_course.class_name).exists():
            return Response({
                "message": f"Already enrolled in a section of {new_course.class_name}."
            }, status=400)

        # Check for day and time conflicts
        for enrolled_course in currently_enrolled:
            # Shared day?
            for day in enrolled_course.Date:
                if day in new_course.Date:
                    # Now also check if time matches
                    if enrolled_course.Time == new_course.Time:
                        return Response({
                            "message": f"Time conflict with {enrolled_course.class_name} on {day} at {new_course.Time}."
                        }, status=400)

        student.enrolled_courses.add(new_course)

        return Response({
            "message": f"Successfully enrolled in {new_course.class_name}."
        })

    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
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

@csrf_exempt
@api_view(['POST'])
def remove_from_cart(request):
    student_id = request.data.get('student_id')
    course_id = request.data.get('course_id')
    

    try:
        student = Student.objects.get(id_number=student_id)
        cart = Cart.objects.get(student=student)
        print(" Cart ID:", cart.id)
        print(" Course ID to remove:", course_id)
        print("CartItem course ID:", CartItem.objects.select_related('course').all())            # should be a string

        cart_item = CartItem.objects.get(cart=cart, course_id=course_id)
        cart_item.delete()

        return Response({"message": "Course removed from cart."})
    except CartItem.DoesNotExist:
        return Response({'error': 'Course not found in cart'}, status=404)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    except CartItem.DoesNotExist:
        return Response({'error': 'Course not found in cart'}, status=404)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
@api_view(["POST"])
def drop_class(request):
    student_id = request.data.get('student_id')
    course_ids = request.data.get('course_ids', [])  # expecting a list

    try:
        student = Student.objects.get(id_number=student_id)

        dropped_courses = []
        not_enrolled_courses = []

        for course_id in course_ids:
            try:
                course = Course.objects.get(id_number=course_id)

                if student.enrolled_courses.filter(id_number=course_id).exists():
                    student.enrolled_courses.remove(course)
                    dropped_courses.append(course.class_name)
                else:
                    not_enrolled_courses.append(course.class_name)

            except Course.DoesNotExist:
                not_enrolled_courses.append(f"Unknown Course ID: {course_id}")

        return Response({
            "message": "Drop operation completed.",
            "dropped_courses": dropped_courses,
            "not_enrolled_courses": not_enrolled_courses
        })

    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
