from rest_framework.routers import DefaultRouter
from app.api.urls import course_router
from django.urls import path, include

router = DefaultRouter()
router.registry.extend(course_router.registry)

urlpatterns = [
    path('', include(router.urls))
]