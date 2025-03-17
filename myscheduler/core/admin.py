from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

# Register your models here.
class Admin(UserAdmin):
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'first_name', 'last_name', 'id_number')
            }
        ),
    )

admin.site.register(Student, Admin)