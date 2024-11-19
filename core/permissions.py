from rest_framework.permissions import BasePermission

class IsColecionador(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.colecionador == request.user