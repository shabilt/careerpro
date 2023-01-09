from django import views
from django.urls import path
from rest_framework import routers
from .views import *

app_name = 'student'

router = routers.DefaultRouter()
router.register('student',StudentViewSet, basename='student')
router.register('specialization',SpecializationViewSet, basename='specialization')
router.register('job-application',JobApplicationViewSet, basename='job_application')
router.register('student-note',StudentNoteViewSet,basename='student_note')
# router.register('admin',AdminViewSet, basename='admin')




urlpatterns=[
    path('dashboard', dashboard, name="dashboard"),
    path('my-profile', my_profile, name="my_profile"),
]

urlpatterns += router.urls

