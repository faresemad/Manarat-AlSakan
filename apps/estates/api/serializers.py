from rest_framework import serializers

from apps.estates.models import Estate, EstateImage


class EstateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateImage
        fields = ("image",)


class EstateSerializer(serializers.ModelSerializer):
    images = EstateImageSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    upload_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Estate
        fields = (
            "id",
            "slug",
            "user",
            "name",
            "property_type",
            "num_rooms",
            "num_bathrooms",
            "total_area",
            "price",
            "location",
            "status",
            "data",
            "description",
            "added_at",
            "additional_info",
            "latitude",
            "longitude",
            "images",
            "upload_images",
        )
        read_only_fields = (
            "id",
            "slug",
            "added_at",
        )

    def create(self, validated_data):
        images = validated_data.pop("upload_images", [])
        estate = Estate.objects.create(**validated_data)
        for image in images:
            EstateImage.objects.create(estates=estate, image=image)
        return estate
