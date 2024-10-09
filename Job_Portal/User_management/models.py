from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('job_seeker', 'job_seeker'),
        ('employer', 'employer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES )
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    resume = models.URLField()
    country = models.CharField(max_length=50)
    job_cate = models.CharField(max_length=50)

    
    def __str__(self):
        return self.user.username

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username