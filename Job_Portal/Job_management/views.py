from rest_framework import generics
from .models import JobPost, JobApplication
from .serializers import JobPostSerializer, JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from User_management.permissions import IsJobSeeker, IsEmployer

class JobPostCreateView(generics.CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated,IsEmployer]

class JobPostListView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

class JobPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated]

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