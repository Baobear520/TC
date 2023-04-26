from rest_framework import permissions

# class CanCreateIfAnonOrSuperUser(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated or self.request.user.is_superuser:
#             return super().has_permission(request, view)