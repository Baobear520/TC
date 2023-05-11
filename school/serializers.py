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
    user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    username = serializers.CharField(source='user.username',read_only=True)
    enrollments = EnrollmentSerializer(many=True,read_only=True)

    class Meta:
        model = Student
        fields = ('user','username','date_of_birth','photo','show_image','enrollments')
        validators = [UniqueTogetherValidator(
            queryset=Student.objects.all(),
            fields=['user'],
            message='Current user already has a student profile'
        )]
    

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
        
    # def get_number_of_currently_enrolled(self,course):
    #     course = Course.objects.
    #     number = Count(Enrollment.objects.filter(course=course,lessons__gt=0))
    #     return number







    
    
    