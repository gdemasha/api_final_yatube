from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return True
