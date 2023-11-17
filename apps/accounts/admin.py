from django.contrib import admin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "national_id", "email", "phone", "role")
    search_fields = ("name", "national_id", "email", "phone", "role")
    list_filter = ("role",)
