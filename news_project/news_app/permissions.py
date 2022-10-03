from rest_framework import permissions

class UserEditPermission(permissions.BasePermission):
    message = 'You allowed to edit only your profile!'

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id