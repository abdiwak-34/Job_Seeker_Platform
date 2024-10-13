from rest_framework import generics
from .models import JobPost, JobApplication
from .serializers import JobPostSerializer, JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from User_management.permissions import IsJobSeeker, IsEmployer
from .permissions import IsJobOwner
from User_management.serializers import JobSeeker, Employer
from User_management.models import EmployerProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

class JobPostCreateView(generics.CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated,IsEmployer]

    def perform_create(self, serializer):
        try:
            employer_profile = EmployerProfile.objects.get(user=self.request.user)
            serializer.save(employer=employer_profile)
        except EmployerProfile.DoesNotExist:
            raise NotFound(detail="Employer profile not found.")
        
class JobPostListView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated, IsJobOwner]

class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated, IsJobSeeker]

class JobApplicationListView(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

class JobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]