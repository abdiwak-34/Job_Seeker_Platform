from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, JobSeekerProfile, EmployerProfile
from .serializers import JobSeekerProfileSerializer, EmployerProfileSerializer, RegisterSerializer, Employer, JobSeeker
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
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class JobSeekerProfileCreateView(generics.CreateAPIView):
    serializer_class = JobSeekerProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsJobSeeker]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerProfileCreateView(generics.CreateAPIView):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateJobSeekerProfileView(generics.UpdateAPIView):
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return JobSeekerProfile.objects.get(user=self.request.user)

class UpdateEmployerProfileView(generics.UpdateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return EmployerProfile.objects.get(user=self.request.user)


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        # Check if user is a job seeker
        if user.role == 'job_seeker':
            try:
                profile = JobSeekerProfile.objects.get(user=user)
                serializer = JobSeeker(profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except JobSeekerProfile.DoesNotExist:
                return Response({"error": "Job seeker profile not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if user is an employer
        elif user.role == 'employer':
            try:
                profile = EmployerProfile.objects.get(user=user)
                serializer = Employer(profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except EmployerProfile.DoesNotExist:
                return Response({"error": "Employer profile not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "User role not recognized."}, status=status.HTTP_400_BAD_REQUEST)
