from rest_framework import permissions

class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'owner'

class CheckClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'client'

class CheckOwnerEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

class CheckCourier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.status == ['courier', 'owner']