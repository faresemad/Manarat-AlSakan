from django.contrib import admin

from apps.estates.models import Estate, EstateImage


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "location",
        "owner",
        "num_units",
        "architecturally_designed",
        "construction_date",
        "created_at",
        "updated_at",
        "request_state",
    ]
    list_filter = [
        "name",
        "location",
        "owner",
        "num_units",
        "architecturally_designed",
        "construction_date",
        "created_at",
        "updated_at",
        "request_state",
    ]
    search_fields = [
        "name",
        "location",
        "owner",
        "num_units",
        "architecturally_designed",
        "construction_date",
        "created_at",
        "updated_at",
        "request_state",
    ]
    readonly_fields = [
        "id",
        "slug",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "name",
        "location",
        "owner",
        "num_units",
        "architecturally_designed",
        "construction_date",
        "created_at",
        "updated_at",
        "request_state",
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
