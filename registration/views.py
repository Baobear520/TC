from rest_framework import generics,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from registration.models import User
from registration.serializers import BaseUserSerializer, ResetPasswordSerializer, UserProfileSerializer,UserRegisterSerializer


@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'create user':reverse('user-create',request=request,format=format),
        'login':reverse('token-obtain_pair',request=request,format=format),
        'refresh':reverse('token-refresh',request=request,format=format),
    })



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

    

class ResetPasswordView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]