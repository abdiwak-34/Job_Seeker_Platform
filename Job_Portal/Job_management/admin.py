from django.contrib import admin
from .models import JobPost, JobApplication

# Register your models here.

admin.site.register(JobApplication)
admin.site.register(JobPost)