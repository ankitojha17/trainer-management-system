import requests
from service.utils.constants import USER_ENRICHMENT_API_URL, EXTERNAL_API_TIMEOUT
from service.utils.exceptions import ExternalServiceError

class UserManagementService:
    """
    Handles communication with external user data providers 
    to enrich trainer profiles.
    """
    @staticmethod
    def fetch_trainer_name_by_email(email):
        try:
            response = requests.get(
                USER_ENRICHMENT_API_URL, 
                timeout=EXTERNAL_API_TIMEOUT
            )
            response.raise_for_status() 
            users = response.json()
            
            for user in users:
                if user.get('email', '').lower() == email.lower():
                    return user.get('name')
            
            return None 
            
        except (requests.RequestException, ValueError):
            raise ExternalServiceError()