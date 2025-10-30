from rest_framework.views import exception_handler
from .utils import format_response, ResponseCode

def custom_exception_handler(exc, context):
    """自定义异常处理"""
    response = exception_handler(exc, context)
    
    if response is not None:
        error_detail = exc.detail if hasattr(exc, 'detail') else str(exc)
        return format_response(
            code=response.status_code,
            msg=error_detail,
            data=None
        )
    
    return format_response(
        code=ResponseCode.INTERNAL_SERVER_ERROR,
        msg="服务器内部错误",
        data=None
    )