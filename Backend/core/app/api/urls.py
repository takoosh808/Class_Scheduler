from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import CourseViewSet,LoginView,UserView

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'login',LoginView,basename='login')
router.register(r'getuser',UserView,basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]