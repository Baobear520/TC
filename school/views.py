from django.shortcuts import get_object_or_404
from rest_framework import generics,permissions,status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from school.models import Student,Enrollment,Course,Level
from school.serializers import StudentSerializer,EnrollmentSerializer,\
CourseSerializer,LevelSerializer
from school.permissions import IsAdminOrReadOnly,IsOwnerOrAdminOrNoAccess

    

class StudentViewSet(CreateModelMixin,viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    permission_classes = []


    @action(detail=False,methods=['GET','PUT'],permission_classes=[permissions.IsAuthenticated])
    def me(self,request):
        (student,created) = Student.objects.get_or_create(
            user_id__username=request.user.username)
        if request.method == 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = StudentSerializer(student,data=request.data,context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
    

class EnrollmentViewSet(RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = []

    @action(detail=False)
    def me(self,request):
        (enrollment,created) = Enrollment.objects.get_or_create(
            student__user_id=request.user.id)
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data)

    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = []
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    


    

    
    
    
        