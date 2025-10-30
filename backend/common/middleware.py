import time
from django.utils.deprecation import MiddlewareMixin
from .utils import format_response, ResponseCode

class RequestLoggingMiddleware(MiddlewareMixin):
    """请求日志中间件"""
    
    def process_request(self, request):
        request.start_time = time.time()
    
    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            print(f"{request.method} {request.path} - {duration:.2f}s")
        return response

class ExceptionHandlingMiddleware(MiddlewareMixin):
    """全局异常处理中间件"""
    
    def process_exception(self, request, exception):
        return format_response(
            code=ResponseCode.INTERNAL_SERVER_ERROR,
            msg="服务器内部错误",
            data=None
        )