from rest_framework.permissions import IsAuthenticated


class IsSeller(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role == "seller"


class IsBuyer(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.role == "buyer"
