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

class JobPostCreateView(generics.CreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [IsAuthenticated,IsEmployer]

    def perform_create(self, serializer):
        try:
            profile = EmployerProfile.objects.get(user=self.request.user)
            serializer = Employer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EmployerProfile.DoesNotExist:
            return Response({"detail": "Employer profile not found."}, status=status.HTTP_400_BAD_REQUEST)
        
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