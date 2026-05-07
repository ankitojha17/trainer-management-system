# service/urls.py
from django.urls import path
from service.views.trainer_views import TrainerCreateView
from service.views.training_module_views import ModuleListCreateView
from service.views.resource_views import ResourceUploadView

urlpatterns = [
    path('trainers', TrainerCreateView.as_view(), name='trainer-create'),
    path('modules', ModuleListCreateView.as_view(), name='module-list-create'),
    path('resources/upload', ResourceUploadView.as_view(), name='resource-upload'),
]