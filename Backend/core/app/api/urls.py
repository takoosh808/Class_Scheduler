from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet,LoginView,UserView, add_to_cart, view_cart, enroll_courses, view_enrolled_courses
from .views import remove_from_cart, drop_class

router = DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/courses/', CourseViewSet.as_view(), name='course-excel'),
    path('api/login/',LoginView,name='login'),
    path('api/getuser/',UserView,name='user'),
    path('api/cart/add/', add_to_cart, name='add_to_cart'),
    path('api/cart/remove/', remove_from_cart, name='remove_from_cart'),
    path('api/enroll/', enroll_courses,name='enroll_courses'),
    path('api/drop/', drop_class,name='drop_class'),
    path('api/cart/<str:student_id>/', view_cart, name='view_cart'),
    path('api/enrolled/<str:student_id>/', view_enrolled_courses,name='view_enrolled_courses'),
]