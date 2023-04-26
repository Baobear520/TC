
from django.conf import settings
from rest_framework.permissions import AllowAny,IsAuthenticated
from djoser import views
#from registration.permissions import CanCreateIfAnonOrSuperUser


# class UserViewSet(views.UserViewSet):
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [AllowAny()]
#         return [IsAuthenticated()]
        
#         