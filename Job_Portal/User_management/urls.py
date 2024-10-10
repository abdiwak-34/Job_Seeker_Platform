from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/retrieve/', UserProfileView.as_view(), name='user-profile'),
    path('profile/jobseeker/create/', JobSeekerProfileCreateView.as_view(), name='jobseeker-profile-create'),
    path('profile/employer/create/', EmployerProfileCreateView.as_view(), name='employer-profile-create'),
    path('update-jobseeker-profile/', UpdateJobSeekerProfileView.as_view(), name='update-jobseeker-profile'),
    path('update-employer-profile/', UpdateEmployerProfileView.as_view(), name='update-employer-profile'),
]
