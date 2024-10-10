from django.db import models
from django.conf import settings
from User_management.models import EmployerProfile, JobSeekerProfile

class JobPost(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='job_posts')
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    job_category = models.CharField(max_length=100)
    qualification = models.CharField(max_length=255)
    skills = models.TextField()
    experience = models.IntegerField(help_text="Years of experience required")
    job_posted_date = models.DateField(auto_now_add=True)
    application_deadline = models.DateField()

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    job_seeker_profile = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField()
    application_date = models.DateField(auto_now_add=True)
    linkedin_profile = models.URLField(max_length=255, null=True, blank=True)
    portfolio = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.job_seeker_profile.user.username} - {self.job_post.title}"
