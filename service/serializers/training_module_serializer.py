from rest_framework import serializers
from django.shortcuts import get_object_or_404
from service.models.training_module import TrainingModule
from service.models.trainer import Trainer
from service.serializers.resource_serializer import ResourceSerializer

class TrainingModuleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_by = serializers.IntegerField(write_only=True)
    trainer_name = serializers.CharField(source='created_by.name', read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)

    def create(self, validated_data):
        trainer = get_object_or_404(Trainer, id=validated_data.pop('created_by'))
        return TrainingModule.objects.create(created_by=trainer, **validated_data)