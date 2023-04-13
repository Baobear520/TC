from django.urls import include, path
from rest_framework import routers
from school import views

urlpatterns = [
    path('students', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('enrollments',views.EnrollmentList.as_view()),
    path('enrollments/<int:pk>',views.EnrollmentDetail.as_view()),
    path('courses',views.CourseList.as_view()),
    path('courses/<int:pk>',views.CourseDetail.as_view()),
    path('levels',views.LevelList.as_view()),
    path('levels/<int:pk>',views.LevelDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/<int:pk>',views.UserDetail.as_view())
]