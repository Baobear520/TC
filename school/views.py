from django.shortcuts import render, get_object_or_404
from school.models import Student,Enrollment

# Create your views here.


def show_students(request):
    query_set = Student.objects.all()
    context = {'students_list': query_set}
    return render(request,'school/show_students.html',context)

def indiv_student(request,student_id):
    student = get_object_or_404(Student,pk=student_id)
    context = {'student': student}
    return render(request,'school/indiv_student.html',context)

def show_enrollments(request):
    query_set = Enrollment.objects.all()
    context = {'enrollments_list': query_set}
    return render(request,'school/show_enrollments.html',context)