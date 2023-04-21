from django.shortcuts import get_object_or_404
from rest_framework import generics,permissions,status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from school.models import Student,Enrollment,Course,Level
from school.serializers import StudentSerializer,EnrollmentSerializer,\
CourseSerializer,LevelSerializer
from school.permissions import IsAdminOrReadOnly

    

class StudentViewSet(CreateModelMixin,viewsets.GenericViewSet):
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
    
    


    

    
    
    
        