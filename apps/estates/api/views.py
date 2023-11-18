from rest_framework import viewsets

from apps.estates.api.serializers import EstateSerializer
from apps.estates.models import Estate


class EstatsViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
