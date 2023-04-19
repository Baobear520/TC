from django.contrib.auth.models import User
from rest_framework import serializers
from school.models import Student,Enrollment,Course,Level

class UserSerializer(serializers.ModelSerializer):              
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user','id','date_of_birth','show_image')
        

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('id','date_enrolled','student','course','lessons','money_paid')






    
    
    