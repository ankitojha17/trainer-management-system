from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

class GlobalExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        logger.error(f"Global Exception Caught: {str(exception)}", exc_info=True)
        return JsonResponse({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred on the server.'
        }, status=500)