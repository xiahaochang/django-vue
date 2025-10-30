from rest_framework import permissions
from common.permissions import IsAdminUser

class IsAdminOrReadOnly(permissions.BasePermission):
    """只有管理员可以修改，其他用户只能查看"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return IsAdminUser().has_permission(request, view)

class UserProfilePermission(permissions.BasePermission):
    """用户可以查看和修改自己的资料，管理员可以查看和修改所有资料"""
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        return obj == request.user