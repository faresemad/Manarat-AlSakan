import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Estate(models.Model):
    class RequestState(models.TextChoices):
        PENDING = "PENDING"
        APPROVED = "APPROVED"
        REJECTED = "REJECTED"

    class PropertyType(models.TextChoices):
        APARTMENT = "APARTMENT"
        BUNGALOW = "BUNGALOW"
        DUPLEX = "DUPLEX"
        FLAT = "FLAT"
        HOUSE = "HOUSE"
        MANSION = "MANSION"
        PENTHOUSE = "PENTHOUSE"
        TERRACED = "TERRACED"
        TOWNHOUSE = "TOWNHOUSE"
        VILLA = "VILLA"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PropertyType.choices)
    num_rooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    total_area = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=RequestState.choices, default=RequestState.PENDING)
    data = models.JSONField(null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-").lower()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Estate"
        verbose_name_plural = "Estates"
        ordering = ["-added_at"]
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
