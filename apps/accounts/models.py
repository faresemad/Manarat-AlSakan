import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        BUYER = "buyer", "Buyer"
        SELLER = "seller", "Seller"

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)
    national_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=UserTypes.choices, default=UserTypes.BUYER)
    USERNAME_FIELD = "national_id"
    REQUIRED_FIELDS = ["name", "email", "phone", "role"]

    class Meta:
        verbose_name_plural = "Users"
        unique_together = ["email", "national_id"]
        indexes = [
            models.Index(fields=["id", "name"]),
        ]
