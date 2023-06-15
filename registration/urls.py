from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView)
from registration import views


urlpatterns = [
    path('users/',views.UserListView.as_view(),name='user-list'),
    path('users/<int:pk>',views.UserDetailView.as_view(),name='user-detail'),
    path('create', views.RegisterView.as_view(),name='user-create'),
    path('login/',TokenObtainPairView.as_view(),name = 'token-obtain_pair'),
    path('login/refresh/',TokenRefreshView.as_view(),name = 'token-refresh'),
]