from rest_framework.exceptions import APIException
from rest_framework import status

class ExternalServiceError(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'The external user service (JSONPlaceholder) is currently unavailable.'
    default_code = 'external_api_failure'

class FileValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid file type or size. Only .pdf and .docx under 2MB are allowed.'
    default_code = 'file_validation_error'