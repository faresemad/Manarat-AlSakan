from django.contrib import admin

from apps.estates.models import Estate, EstateImage


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "property_type",
        "num_rooms",
        "num_bathrooms",
        "total_area",
        "price",
        "location",
        "status",
        "data",
        "description",
        "slug",
        "added_at",
        "additional_info",
        "latitude",
        "longitude",
        "user",
    ]
    list_filter = [
        "name",
        "property_type",
        "num_rooms",
        "num_bathrooms",
        "total_area",
        "price",
        "location",
        "status",
        "data",
        "description",
        "slug",
        "added_at",
        "additional_info",
        "latitude",
        "longitude",
        "user",
    ]
    search_fields = [
        "name",
        "property_type",
        "num_rooms",
        "num_bathrooms",
        "total_area",
        "price",
        "location",
        "status",
        "data",
        "description",
        "slug",
        "added_at",
        "additional_info",
        "latitude",
        "longitude",
        "user",
    ]
    readonly_fields = ["id", "slug", "added_at"]
    ordering = [
        "name",
        "property_type",
        "num_rooms",
        "num_bathrooms",
        "total_area",
        "price",
        "location",
        "status",
        "data",
        "description",
        "slug",
        "added_at",
        "additional_info",
        "latitude",
        "longitude",
        "user",
    ]
    list_per_page = 25


@admin.register(EstateImage)
class EstateImageAdmin(admin.ModelAdmin):
    list_display = ["estates", "image"]
    list_filter = ["estates"]
    search_fields = ["estates"]
    readonly_fields = ["id"]
    ordering = ["estates"]
    list_per_page = 25
