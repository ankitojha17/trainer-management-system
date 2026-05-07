from rest_framework import generics
from service.models.training_module import TrainingModule
from service.serializers.training_module_serializer import TrainingModuleSerializer
from service.utils.pagination import StandardResultsPagination

class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = TrainingModule.objects.select_related('created_by').prefetch_related('resources').all()
    serializer_class = TrainingModuleSerializer
    pagination_class = StandardResultsPagination