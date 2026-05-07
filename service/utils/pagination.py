from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class StandardResultsPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'
    max_page_size = 20

    def paginate_queryset(self, queryset, request, view=None):
        try:
            return super().paginate_queryset(queryset, request, view)
        except NotFound:
           
            return []

    def get_paginated_response(self, data):
        count = getattr(self.page.paginator, 'count', 0) if hasattr(self, 'page') else 0
        total_pages = getattr(self.page.paginator, 'num_pages', 1) if hasattr(self, 'page') else 1
        current_page = int(self.request.query_params.get('page', 1))
        msg = "Data retrieved successfully" if data else "No data found on this page"

        return Response({
            'status': 'success',
            'message': msg,
            'metadata': {
                'total_count': count,
                'total_pages': total_pages,
                'current_page': current_page,
                'next': self.get_next_link() if data else None,
                'previous': self.get_previous_link() if data else None,
            },
            'results': data
        })