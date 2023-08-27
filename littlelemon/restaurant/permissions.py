from rest_framework import permissions

class AdminOrManagerPermission(permissions.BasePermission):
    permission_name = 'Manager'
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='Manager').exists()