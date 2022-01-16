from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsCreatorOrReadOnly(BasePermission):
    """ customer permissions to only allow creators of competitions to edit them """
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed to anyone so allow GET, HEAD, or OPTIONS requests
        if request.method in SAFE_METHODS:
            return True
        return obj.creator == request.user

