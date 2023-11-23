# Generated by Django 4.2 on 2023-11-23 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Estate",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("APARTMENT", "Apartment"),
                            ("BUNGALOW", "Bungalow"),
                            ("DUPLEX", "Duplex"),
                            ("FLAT", "Flat"),
                            ("HOUSE", "House"),
                            ("MANSION", "Mansion"),
                            ("PENTHOUSE", "Penthouse"),
                            ("TERRACED", "Terraced"),
                            ("TOWNHOUSE", "Townhouse"),
                            ("VILLA", "Villa"),
                        ],
                        max_length=20,
                    ),
                ),
                ("num_rooms", models.IntegerField()),
                ("num_bathrooms", models.IntegerField()),
                ("total_area", models.FloatField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("location", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("APPROVED", "Approved"), ("REJECTED", "Rejected")],
                        default="PENDING",
                        max_length=10,
                    ),
                ),
                ("data", models.JSONField(blank=True, null=True)),
                ("description", models.TextField()),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                ("additional_info", models.TextField(blank=True, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Estate",
                "verbose_name_plural": "Estates",
                "ordering": ["-added_at"],
            },
        ),
        migrations.CreateModel(
            name="EstateImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to="estates_images/")),
                (
                    "estates",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="images", to="estates.estate"
                    ),
                ),
            ],
            options={
                "verbose_name": "Estate Image",
                "verbose_name_plural": "Estate Images",
            },
        ),
        migrations.AddIndex(
            model_name="estate",
            index=models.Index(fields=["id", "name", "location"], name="estates_est_id_867e43_idx"),
        ),
        migrations.AlterUniqueTogether(
            name="estate",
            unique_together={("name", "location")},
        ),
    ]
