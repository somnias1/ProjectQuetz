from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS

# SAFE_METHODS are get, post and head


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.autor == request.user


class IsTutorialOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.tutorial_padre.autor == request.user


class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.comentador == request.user


class IsReplyOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.comentador_respuesta == request.user


class IsAnnounceOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.comunicador == request.user
