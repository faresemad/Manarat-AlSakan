from django.contrib import admin  # noqa

from apps.estates.models import Estate, EstateImage

# Register your models here.

admin.site.register(Estate)
admin.site.register(EstateImage)
