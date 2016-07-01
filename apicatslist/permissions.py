from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CanPost(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj is None or obj.user == request.user
