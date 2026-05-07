from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from .models.trainer import Trainer
from .models.training_module import TrainingModule
import requests
from unittest.mock import patch

class TrainingProjectTests(TestCase):
    def setUp(self):
        """Initial setup for all test cases."""
        self.client = APIClient()
        self.trainer = Trainer.objects.create(
            name="Test Trainer", 
            email="admin@test.com"
        )
        self.module = TrainingModule.objects.create(
            title="Django Advanced",
            description="Professional Modular Architecture",
            created_by=self.trainer
        )

    
    def test_file_size_validation(self):
        """Verify that files larger than 2MB are rejected."""
        large_content = b"x" * int(2.1 * 1024 * 1024) 
        large_file = SimpleUploadedFile("manual.pdf", large_content, content_type="application/pdf")
        
        response = self.client.post('/api/resources/upload/', {
            'file': large_file, 
            'name': 'Big File',
            'module_ids': [self.module.id]
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_extension(self):
        """Verify that non-supported file extensions are rejected."""
        bad_file = SimpleUploadedFile("script.py", b"print('hello')", content_type="text/x-python")
        
        response = self.client.post('/api/resources/upload/', {
            'file': bad_file, 
            'name': 'Python Script'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('service.api_integration_logic.external_api.requests.get')
    def test_trainer_creation_with_api_enrichment(self, mock_get):
        """Test success path: Trainer name is fetched from JSONPlaceholder."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {'email': 'Sincere@april.biz', 'name': 'Leanne Graham'}
        ]

        response = self.client.post('/api/trainers/', {'email': 'Sincere@april.biz'})
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Leanne Graham')

    @patch('service.api_integration_logic.external_api.requests.get')
    def test_trainer_creation_api_timeout_logic(self, mock_get):
        """Test failure path: Logic returns 503 if external API fails."""
        mock_get.side_effect = requests.exceptions.RequestException("Connection Timeout")

        response = self.client.post('/api/trainers/', {'email': 'timeout@test.com'})
        
        self.assertEqual(response.status_code, status.HTTP_503_SERVICE_UNAVAILABLE)

    def test_module_list_pagination(self):
        """Ensure the module list view is paginated."""
        response = self.client.get('/api/modules/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_module_ordering(self):
        """Verify that modules exist and are returned in the result set."""
        response = self.client.get('/api/modules/')
        self.assertEqual(len(response.data['results']), 1)