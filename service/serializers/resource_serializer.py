from rest_framework import serializers
from service.models.resource import Resource

class ResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    file = serializers.FileField()

    def create(self, validated_data):
        return Resource.objects.create(**validated_data)