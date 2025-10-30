from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """只允许管理员访问"""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsOwnerOrAdmin(permissions.BasePermission):
    """只允许对象所有者或管理员访问"""
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        
        if hasattr(obj, 'user'):
            return obj.user == request.user
        elif hasattr(obj, 'id'):
            return obj.id == request.user.id
        
        return False

class ReadOnly(permissions.BasePermission):
    """只读权限"""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS