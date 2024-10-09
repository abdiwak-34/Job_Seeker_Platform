from rest_framework import permissions


class IsJobSeeker(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.role == 'job_seeker'


class IsEmployer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.role == 'employer'
