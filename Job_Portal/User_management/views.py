from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, JobSeekerProfile, EmployerProfile
from .serializers import JobSeekerProfileSerializer, EmployerProfileSerializer, RegisterSerializer
from .permissions import IsJobSeeker, IsEmployer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class JobSeekerProfileCreateView(generics.CreateAPIView):
    serializer_class = JobSeekerProfileSerializer
    permission_classes = [IsAuthenticated, IsJobSeeker]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerProfileCreateView(generics.CreateAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
