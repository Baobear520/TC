from django.conf import settings
from django.db.models import Count
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from school.models import Student,Enrollment,Course,Level


class EnrollmentSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    class Meta:
        model = Enrollment
        fields = ('date_enrolled','course','lessons','money_paid')

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    enrollments = EnrollmentSerializer(many=True,read_only=True)

    class Meta:
        model = Student
        fields = ('username','date_of_birth','photo','show_image','enrollments','display_grade')
        
    def create(self, validated_data):
          student = Student.objects.create(
            user_id=self.context['request'].user.id,
             **validated_data)
          return student
        

        
        
class LevelSerializer(serializers.ModelSerializer):
    available_courses = serializers.StringRelatedField(many=True)
    
        
    class Meta:
        model = Level
        fields = ('title','description','available_courses')

class CourseSerializer(serializers.ModelSerializer):
    level = serializers.StringRelatedField()
    number_of_currently_enrolled = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Course
        fields = ('title','level','description','number_of_classes','price','number_of_currently_enrolled')
        
  







    
    
    