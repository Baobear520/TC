from django.urls import include, path
from rest_framework import routers
from school import views

urlpatterns = [
    path('students', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
]