
from django.db.models import OuterRef,Count,Q
from django.shortcuts import get_object_or_404
from rest_framework import generics,permissions,status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from school.models import Student,Enrollment,Course,Level
from school.serializers import StudentSerializer,EnrollmentSerializer,\
CourseSerializer,LevelSerializer

    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'me'
  
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
  
         
    @action(detail=False,methods=['GET','PUT'],permission_classes=[permissions.IsAuthenticated])
    def me(self,request):
        (student,created) = Student.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        elif request.method == 'PUT':
                serializer = StudentSerializer(
                        student,data=request.data,
                        context={'request': request})
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return Response(serializer.data)
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('level').annotate(
        number_of_currently_enrolled=Count('enrollment',
        filter=Q(enrollment__lessons__gte=1)
        )
    )
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
    


    

    
    
    
        