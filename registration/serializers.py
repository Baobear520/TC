from django.contrib.auth.password_validation import validate_password
from django.urls import reverse
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from registration.models import User

class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedIdentityField(view_name='user-detail',format='html')

    class Meta:
        model = User
        fields = ('username','status','profile') 

class UserProfileSerializer(serializers.ModelSerializer):
    student_profile = serializers.SerializerMethodField()
    reset_password = serializers.HyperlinkedIdentityField(
        view_name='reset-password',
        format='html'
    )

    def get_student_profile(self, obj):
        student = obj.student
        if obj.status == 'Student' and hasattr(obj,'student'):
            # Assuming the student detail URL is named 'student-detail'
            return self.context['request'].build_absolute_uri(reverse(
                'student-detail',args=['me'])
            ) 
        return None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','student_profile','reset_password')

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
     
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Passwords don't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class ResetPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    new_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
     )
    class Meta:
        model = User
        fields = ('old_password','new_password','confirm_password')

    def validate(self, attrs):
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({'Validation_error':'New password is the same.Please provide a different one.'})
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'Validation_error': "Passwords don't match."})
        return super().validate(attrs)
        

        

    
    
    

    
   



