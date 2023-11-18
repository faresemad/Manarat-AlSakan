from django.contrib import admin  # noqa

from apps.estates.models import Building, BuildingImage

# Register your models here.

admin.site.register(Building)
admin.site.register(BuildingImage)
