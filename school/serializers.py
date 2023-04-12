from django.contrib.auth.models import User,Group
from rest_framework import serializers
from school.models import Student,Enrollment,Course,Level

#class UserSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = User
        #fields = ['url','username','email','groups']


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Group
        #fields = ['url','name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        

    
    
    