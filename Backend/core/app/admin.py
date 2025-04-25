from django.contrib import admin
from . models import Course, Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'first_name', 'last_name') 
    search_fields = ('first_name', 'last_name', 'id_number')
    readonly_fields = ('enrolled_summary',)
    filter_horizontal = ('enrolled_courses',)

    def enrolled_summary(self, obj):
        return "\n".join([f"{c.class_name} ({c.id_number})" for c in obj.enrolled_courses.all()])

    enrolled_summary.short_description = "Enrolled Courses (View Only)"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'class_name', 'IsLab', 'Section_Number', 'Instructor', 'Location', 'Date', 'Time','Enrollment_max', 'Enrollment' ) 
    search_fields = ('id_number', 'class_name')
    readonly_fields = ('course_summary',)

    def course_summary(self, obj):
        students = obj.enrolled_students.all()
        if not students:
            return "No students enrolled."
        return "\n".join([f"{student.first_name} {student.last_name} ({student.id_number})" for student in students])

    course_summary.short_description = "Enrolled Students (View Only)"