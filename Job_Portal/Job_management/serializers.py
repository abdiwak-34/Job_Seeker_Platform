from rest_framework import serializers
from .models import JobPost, JobApplication

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'company_name', 'job_location', 'job_category', 
                  'qualification', 'skills', 'experience', 'application_deadline']
        read_only_fields = ['employer']
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'