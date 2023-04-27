
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError
from djoser.serializers import UserCreateSerializer as BaseCreateUserSerializer, UserSerializer, UserDeleteSerializer as BaseUserDeleteSerializer
from rest_framework import serializers,status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from registration.models import User


class UserCreateSerializer(BaseCreateUserSerializer):
    #username = serializers.CharField(max_length=150)
    #password = serializers.CharField(required=True,write_only=True)
    #password2 = serializers.CharField(required=True,write_only=True)
    class Meta(BaseCreateUserSerializer.Meta):
        model = User
        fields = ['id','username','password','email','first_name','last_name']
    

    # def validate_password_input(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"Error": "Passwords don't match"})
    #     return attrs


    def create(self, validated_data):
        user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
                )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserRetrieveSerializer(UserSerializer):
    username = serializers.CharField(
        max_length=150)
    
    class Meta(UserSerializer.Meta):
        fields = ['id','username','email','first_name','last_name']
        
   



