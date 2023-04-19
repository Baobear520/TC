from django.contrib.auth.models import User,Group
from django.shortcuts import get_object_or_404

from rest_framework import generics,permissions,status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import action
from school.models import Student,Enrollment,Course,Level
from school.serializers import StudentSerializer,EnrollmentSerializer,\
CourseSerializer,LevelSerializer, UserSerializer
from school.permissions import IsAdminOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    permission_classes = []


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = []
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = []
    
    


    

    
    
    
        