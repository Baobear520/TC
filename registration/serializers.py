from djoser.serializers import UserCreateSerializer as BaseCreateUserSerializer, UserSerializer
from rest_framework import serializers
from registration.models import User


class UserCreateSerializer(BaseCreateUserSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    
    class Meta(BaseCreateUserSerializer.Meta):
        fields = ['id','username','password','password2','email','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Error": "Passwords don't match"})
        return attrs
    
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
    class Meta(UserSerializer.Meta):
        fields = ['id','username','email','first_name','last_name']

