# customiza response for djoser
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(DjoserUserViewSet):
    @action(["post"], detail=False)
    def set_password(self, request, *args, **kwargs):
        response = super().set_password(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"status": "password changed successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(response.data, status=response.status_code)

    @action(["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        response = super().resend_activation(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"status": "activation email sent"}, status=status.HTTP_200_OK)
        else:
            return Response(response.data, status=response.status_code)
