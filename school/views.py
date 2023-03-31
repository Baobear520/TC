
from django.db.models import Exists,OuterRef
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView,DetailView
from school.models import Student,Enrollment

# Create your views here.
class StudentsView(ListView):
    model = Student
    template_name = 'school/show_students.html'
    context_object_name = 'students_list'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/indiv_student.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enrollment_list = Enrollment.objects.filter(student=self.kwargs['pk'])
        context['enrollment_list'] = enrollment_list
        context['current_enrollments'] = enrollment_list.filter(lessons__gt=0) 
        return context

    
class EnrollmentsListView(ListView):
    model = Enrollment
    template_name = 'school/show_enrollments.html'
    context_object_name = 'enrollments_list'

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'school/indiv_enrollment.html'

    

