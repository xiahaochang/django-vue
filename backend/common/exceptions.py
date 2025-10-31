# exceptions.py
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed, PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from common.utils import ResponseCode  # 假设ResponseCode在你的common.utils中

def custom_exception_handler(exc, context):
    # 先调用DRF默认的异常处理
    response = exception_handler(exc, context)

    # 如果是认证失败或权限拒绝，我们自定义响应格式
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed, PermissionDenied)):
        return Response({
            'code': ResponseCode.UNAUTHORIZED,  # 你可以根据实际情况调整code
            'msg': '未授权访问，请先登录',
            'data': None
        }, status=status.HTTP_401_UNAUTHORIZED)

    # 对于其他异常，如果DRF的异常处理已经处理了，我们就调整格式
    if response is not None:
        # 如果响应已经有数据，我们按照统一格式包装
        response.data = {
            'code': response.status_code,
            'msg': str(exc) if str(exc) else '请求错误',
            'data': None
        }

    # 如果response为None，说明是未处理的异常，我们可以返回一个统一的500错误
    else:
        # 你可以根据需要记录日志
        response = Response({
            'code': ResponseCode.INTERNAL_SERVER_ERROR,
            'msg': '服务器内部错误',
            'data': None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response