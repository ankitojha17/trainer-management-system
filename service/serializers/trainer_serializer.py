from rest_framework import serializers
from service.models.trainer import Trainer

class TrainerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField(required=False, allow_blank=True)