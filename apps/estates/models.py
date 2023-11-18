import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Building(models.Model):
    class RequestState(models.TextChoices):
        PENDING = "PENDING"
        APPROVED = "APPROVED"
        REJECTED = "REJECTED"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    description = models.JSONField()
    slug = models.SlugField(max_length=255, unique=True)
    num_units = models.IntegerField()
    architecturally_designed = models.BooleanField(default=True)
    construction_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request_state = models.CharField(max_length=10, choices=RequestState.choices, default=RequestState.PENDING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["id", "name", "location"]),
        ]
        unique_together = ["name", "location"]


class BuildingImage(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="building_images/")

    def __str__(self):
        return self.building.name

    class Meta:
        verbose_name_plural = "Building Images"
        verbose_name = "Building Image"
