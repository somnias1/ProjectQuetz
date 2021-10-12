from rest_framework.permissions import BasePermission, SAFE_METHODS

# SAFE_METHODS are get, post and head


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.autor == request.user


class IsTutorialOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the device.
        return obj.paso_tutorial.autor == request.user
