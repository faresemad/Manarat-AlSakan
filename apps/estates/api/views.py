from rest_framework import viewsets

from apps.estates.api.serializers import EstateSerializer
from apps.estates.models import Estate
from apps.utils.permissions import IsOwnerOrReadOnly, IsSeller


class EstatsViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsSeller]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]
