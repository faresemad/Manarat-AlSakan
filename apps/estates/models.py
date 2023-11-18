import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Estate(models.Model):
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
        verbose_name = "Estate"
        verbose_name_plural = "Estates"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["id", "name", "location"]),
        ]
        unique_together = ["name", "location"]


class EstateImage(models.Model):
    estates = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="estates_images/")

    def __str__(self):
        return self.estates.name

    class Meta:
        verbose_name_plural = "Estate Images"
        verbose_name = "Estate Image"
