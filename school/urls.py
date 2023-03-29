from django.urls import path
from . import views


urlpatterns = [
    path('students',views.StudentsView.as_view(), name='show students'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(),name='individual student'), 
    path('enrollments',views.EnrollmentsListView.as_view(), name='show enrollments'),]