from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .utils import ResponseCode

class StandardPagination(PageNumberPagination):
    """
    标准分页器 - 页码和大小由请求参数动态指定
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response({
            'code': ResponseCode.SUCCESS,
            'msg': '获取成功',
            'data': {
                'count': self.page.paginator.count,
                'total_pages': self.page.paginator.num_pages,
                'current_page': self.page.number,
                'page_size': self.get_page_size(self.request),
                'has_next': self.page.has_next(),
                'has_previous': self.page.has_previous(),
                'next_page': self.page.next_page_number() if self.page.has_next() else None,
                'previous_page': self.page.previous_page_number() if self.page.has_previous() else None,
                'results': data
            }
        })
    
    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                page_size = int(request.query_params.get(self.page_size_query_param, self.page_size))
                return min(page_size, self.max_page_size)
            except (ValueError, TypeError):
                pass
        return self.page_size