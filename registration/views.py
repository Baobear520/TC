from django.shortcuts import redirect
from rest_framework import viewsets,generics,permissions
from registration.models import User
from registration.serializers import BaseUserSerializer, UserProfileSerializer,UserRegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all() 
    serializer_class = BaseUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.get_queryset()
        else:
            user = self.request.user
        return self.queryset.filter(pk=user.pk)
  
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]




    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]