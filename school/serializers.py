from django.conf import settings
from rest_framework import serializers
from school.models import Student,Enrollment,Course,Level

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('date_enrolled','course','lessons','money_paid')

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    enrollments = EnrollmentSerializer(many=True,read_only=True)
    
    class Meta:
        model = Student
        fields = ('username','date_of_birth','photo','show_image','enrollments')

    def save(self, **kwargs):
        user = self.context['request'].user
        if Student.objects.filter(user_id=user.id).exists():
            raise serializers.ValidationError({'Error':'Current user already has a student profile'})
        student = Student.objects.create(
            user_id=user.id,
            kwargs=self.validated_data)
        return student



        
        
class LevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Level
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        







    
    
    