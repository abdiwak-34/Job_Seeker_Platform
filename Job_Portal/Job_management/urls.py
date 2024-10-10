from django.urls import path
from .views import JobPostCreateView, JobPostListView, JobPostDetailView, JobApplicationCreateView, JobApplicationListView, JobApplicationDetailView

urlpatterns = [
    path('job-posts/', JobPostListView.as_view(), name='job_post_list'),
    path('job-posts/create/', JobPostCreateView.as_view(), name='job_post_create'),
    path('job-posts/<int:pk>/', JobPostDetailView.as_view(), name='job_post_detail'),
    
    path('job-applications/', JobApplicationListView.as_view(), name='job_application_list'),
    path('job-applications/create/', JobApplicationCreateView.as_view(), name='job_application_create'),
    path('job-applications/<int:pk>/', JobApplicationDetailView.as_view(), name='job_application_detail'),
]
