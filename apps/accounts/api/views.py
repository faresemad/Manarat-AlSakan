from rest_framework import mixins, viewsets

from apps.accounts.api.serializers import UserSerializer
from apps.accounts.models import User


class UserViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
