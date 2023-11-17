from django.contrib import admin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "national_id", "email", "phone", "role")
    search_fields = ("username", "national_id", "email", "phone", "role")
    list_filter = ("role",)
