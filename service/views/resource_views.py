from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.models.resource import Resource
from service.serializers.resource_serializer import ResourceSerializer

class ResourceUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResourceSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        resource = serializer.save()
        
        module_ids = request.data.getlist('module_ids')
        resource.modules.set(module_ids) 

        return Response(
            ResourceSerializer(resource).data, 
            status=status.HTTP_201_CREATED
        )