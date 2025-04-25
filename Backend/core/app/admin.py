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