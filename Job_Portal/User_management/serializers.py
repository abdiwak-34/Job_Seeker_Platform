from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, JobSeekerProfile, EmployerProfile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = ['resume', 'job_cate', 'country']
        read_only_fields = ['user']

# Employer Profile Serializer
class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'country']
        read_only_fields = ['user']


from django.contrib.auth import get_user_model

User = get_user_model()

class JobSeeker(serializers.ModelSerializer):
    # Add fields from the User model
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = JobSeekerProfile
        fields = ['first_name', 'last_name', 'email', 'resume', 'country', 'job_cate']
class Employer(serializers.ModelSerializer):
    # Add fields from the User model
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = EmployerProfile
        fields = ['first_name', 'last_name', 'email', 'country', 'company_name']

