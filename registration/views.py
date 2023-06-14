
from rest_framework import viewsets,generics
from registration.models import User
from registration.serializers import UserSerializer,UserRegisterSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer