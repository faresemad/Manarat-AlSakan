from django_filters import FilterSet

from apps.estates.models import Estate


class EstateFilter(FilterSet):
    class Meta:
        model = Estate
        fields = {
            "name": ["exact", "icontains"],
            "property_type": ["exact"],
            "num_rooms": ["exact", "gte", "lte"],
            "num_bathrooms": ["exact", "gte", "lte"],
            "total_area": ["exact", "gte", "lte"],
            "price": ["exact", "gte", "lte"],
            "location": ["exact", "icontains"],
            "status": ["exact"],
            "description": ["exact", "icontains"],
            "added_at": ["exact", "gte", "lte"],
            "additional_info": ["exact", "icontains"],
            "latitude": ["exact", "gte", "lte"],
            "longitude": ["exact", "gte", "lte"],
        }
