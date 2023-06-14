from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView)
from registration import views


router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet,basename='user') 

urlpatterns = [
    path('',include (router.urls)),
    path('create', views.RegisterView.as_view(),name='create_user'),
    path('login/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('login/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
]