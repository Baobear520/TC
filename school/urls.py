from django.urls import include, path
from rest_framework import routers
from school import views

urlpatterns = [
    path('students', views.student_list),
    path('students/<int:pk>/', views.student_detail),
]