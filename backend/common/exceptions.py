from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from .utils import format_response


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    """
    # 调用DRF默认的异常处理
    response = exception_handler(exc, context)
    
    if response is not None:
        # 使用统一响应格式
        return format_response(
            code=response.status_code,
            msg=str(exc) if hasattr(exc, 'detail') else "请求处理失败",
            data=None,
            http_status=response.status_code
        )
    
    # 处理非DRF异常
    return format_response(
        code=500,
        msg="服务器内部错误",
        data=None,
        http_status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )