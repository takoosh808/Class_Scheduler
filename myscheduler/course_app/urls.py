from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("courses", views.courses, name = "courses"),
    path("course_detail/<slug:slug>", views.course_detail, name="course_detail")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)