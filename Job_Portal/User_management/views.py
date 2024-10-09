from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, JobSeekerProfile, EmployerProfile
from .serializers import JobSeekerProfileSerializer, EmployerProfileSerializer, RegisterSerializer
from .permissions import IsJobSeeker, IsEmployer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class JobSeekerProfileCreateView(generics.CreateAPIView):
    serializer_class = JobSeekerProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerProfileCreateView(generics.CreateAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
