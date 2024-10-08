from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('profile/jobseeker/create/', JobSeekerProfileCreateView.as_view(), name='jobseeker-profile-create'),
    path('profile/employer/create/', EmployerProfileCreateView.as_view(), name='employer-profile-create'),
]
