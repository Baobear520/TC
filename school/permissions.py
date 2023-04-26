from rest_framework import permissions
from school.models import Student,Enrollment

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

class IsOwnerOrAdminOrNoAccess(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return super().has_permission(request, view)
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            print(request.user.id,obj.student)
            return request.user == obj.student
        
        
