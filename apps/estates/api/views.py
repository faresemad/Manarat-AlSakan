from rest_framework import viewsets

from apps.estates.api.serializers import EstateRatingCreateSerializer, EstateRatingListSerializer, EstateSerializer
from apps.estates.filters import EstateFilter
from apps.estates.models import Estate, EstateRating
from apps.utils.permissions import IsOwnerOrReadOnly, IsSeller


class EstatsViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.filter(status=Estate.RequestState.APPROVED)
    serializer_class = EstateSerializer
    filterset_class = EstateFilter
    lookup_field = "slug"

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsSeller]
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class EstateRatingViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return EstateRating.objects.filter(estates__slug=self.kwargs["estate_slug"], user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return EstateRatingListSerializer
        return EstateRatingCreateSerializer
