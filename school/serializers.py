from django.conf import settings
from rest_framework import serializers
from school.models import Student,Enrollment,Course,Level



class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Student
        fields = ('user_id','username','date_of_birth','photo','show_image')
    
    # def validate(self, attrs):
    #     user = self.context['request'].user
    #     if Student.objects.filter(user_id=user).exists(): 
    #         raise serializers.ValidationError({'Error': 'This user already has a student profile.'})
        
    #     return attrs

    def create(self,validated_data):
        user = self.context['request'].user
        student = Student.objects.create(
            user=user,
            **validated_data,
        )
        return student

# class StudentProfileViewSerializer(StudentSerializer):
#     class Meta(StudentSerializer.Meta):
#         fields = ['']


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
        fields = ('date_enrolled','student','course','lessons','money_paid')






    
    
    