from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from service.integrations.user_service import UserManagementService
from service.models.trainer import Trainer
from service.serializers.trainer_serializer import TrainerSerializer

class TrainerCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TrainerSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        v_data = serializer.validated_data
        email = v_data.get('email')
        
        api_name = UserManagementService.fetch_trainer_name_by_email(email)
        name = api_name or v_data.get('name')

        if not name:
            return Response({"detail": "Name required."}, status=400)

        trainer, created = Trainer.objects.get_or_create(email=email, defaults={'name': name})

        if not created:
            return Response({"detail": "Trainer already exists."}, status=400)

        return Response(TrainerSerializer(trainer).data, status=status.HTTP_201_CREATED)