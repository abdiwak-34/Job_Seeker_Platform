# Generated by Django 5.0.3 on 2024-10-10 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("User_management", "0002_alter_user_role"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("company_name", models.CharField(max_length=255)),
                ("job_location", models.CharField(max_length=255)),
                ("job_category", models.CharField(max_length=100)),
                ("qualification", models.CharField(max_length=255)),
                ("skills", models.TextField()),
                (
                    "experience",
                    models.IntegerField(help_text="Years of experience required"),
                ),
                ("job_posted_date", models.DateField(auto_now_add=True)),
                ("application_deadline", models.DateField()),
                (
                    "employer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_posts",
                        to="User_management.employerprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cover_letter", models.TextField()),
                ("application_date", models.DateField(auto_now_add=True)),
                (
                    "linkedin_profile",
                    models.URLField(blank=True, max_length=255, null=True),
                ),
                ("portfolio", models.URLField(blank=True, max_length=255, null=True)),
                (
                    "job_seeker_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="User_management.jobseekerprofile",
                    ),
                ),
                (
                    "job_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="Job_management.jobpost",
                    ),
                ),
            ],
        ),
    ]
