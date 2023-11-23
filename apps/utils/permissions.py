from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated


class IsSeller(IsAuthenticated):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) == "seller"


class IsBuyer(IsAuthenticated):
    def has_permission(self, request, view):
        return getattr(request.user, "role", None) == "buyer"


class IsOwnerOrReadOnly(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or isinstance(request.user, AnonymousUser)
