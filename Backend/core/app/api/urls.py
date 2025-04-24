from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import CourseViewSet,LoginView

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'login',LoginView,basename='login')

urlpatterns = [
    path('api/', include(router.urls)),
]