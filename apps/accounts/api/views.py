from rest_framework import viewsets

from apps.accounts.api.serializers import UserSerializer
from apps.accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ["name", "national_id", "email", "phone", "role"]
    # ordering_fields = ["name", "national_id", "email", "phone", "role"]
    # pagination_class = UserPagination
