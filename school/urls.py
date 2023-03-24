from django.urls import path
from . import views

urlpatterns = [
    path('students',views.show_students, name='show students'),
    path('enrollments',views.show_enrollments, name='show enrollments'),
    path('<int:student_id>/', views.indiv_student,name='individual student')]   