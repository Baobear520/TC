from django.contrib.auth.password_validation import validate_password
from django.urls import reverse
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from registration.models import User

class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedIdentityField(view_name='user-detail',format='html')

    class Meta:
        model = User
        fields = ('username','status','profile') 

class UserProfileSerializer(serializers.ModelSerializer):
    student_profile = serializers.SerializerMethodField()

    def get_student_profile(self, obj):
        if obj.status == 'Student' and hasattr(obj, 'student'):
            # Assuming the student detail URL is named 'student-detail'
            return reverse('student-detail', args=[obj.student.pk])
        return None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','student_profile')

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


        

        

    
    
    

    
   



