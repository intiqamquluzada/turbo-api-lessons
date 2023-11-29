from rest_framework import serializers
from turbo.models import Car, CarImages

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = "__all__"