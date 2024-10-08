from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, JobSeekerProfile, EmployerProfile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            password=make_password(validated_data['password']),
        )
        return user

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = ['user', 'resume', 'job_cate', 'country']

# Employer Profile Serializer
class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['user', 'company_name', 'country']
