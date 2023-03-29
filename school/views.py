from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView,DetailView
from school.models import Student,Enrollment

# Create your views here.
class StudentsView(ListView):
    model = Student
    template_name = 'school/show_students.html'
    context_object_name = 'students_list'

    #def get_queryset(self):
        #return Student.objects.all()

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/indiv_student.html'

class EnrollmentsListView(ListView):
    model = Enrollment
    template_name = 'school/show_enrollments.html'
    context_object_name = 'enrollments_list'

    #def get_queryset(self):
        #return Enrollment.objects.all()

