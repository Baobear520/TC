from django.conf import settings
from rest_framework import serializers
from school.models import Student,Enrollment,Course,Level



class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ('user_id','date_of_birth','show_image')


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






    
    
    