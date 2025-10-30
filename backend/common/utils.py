import re
import hashlib
import jwt
import datetime
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response


def md5_encrypt(password):
    """
    MD5加密函数
    Args:
        password: 明文密码
    Returns:
        MD5加密后的字符串
    """
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def format_response(code, msg, data=None, http_status=None):
    """
    统一响应格式封装
    Args:
        code: 业务状态码
        msg: 响应消息
        data: 响应数据
        http_status: HTTP状态码，如果为None则根据code自动推断
    Returns:
        DRF Response对象
    """
    response_data = {
        'code': code,
        'msg': msg,
        'data': data
    }
    
    # 如果没有指定HTTP状态码，则根据code自动推断
    if http_status is None:
        if code >= 200 and code < 300:
            http_status = status.HTTP_200_OK
        elif code == 201:
            http_status = status.HTTP_201_CREATED
        elif code >= 400 and code < 500:
            http_status = status.HTTP_400_BAD_REQUEST
        elif code >= 500:
            http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            http_status = status.HTTP_200_OK
    
    return Response(response_data, status=http_status)

def generate_jwt_token(user):
    """
    生成JWT Token
    Args:
        user: 用户对象
    Returns:
        JWT token字符串
    """
    # 设置token过期时间（24小时后）
    expiration_time = datetime.datetime.utcnow() + settings.JWT_CONFIG['EXPIRATION_DELTA']
    
    # 构建payload
    payload = {
        'user_id': str(user.id),
        'username': user.username,
        'exp': expiration_time,
        'iat': datetime.datetime.utcnow()
    }
    
    # 生成token（需要设置SECRET_KEY）
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_CONFIG['ALGORITHM'])
    return token

def verify_password(input_password, stored_encrypted_password):
    """
    验证密码
    Args:
        input_password: 用户输入的密码
        stored_encrypted_password: 数据库中存储的加密密码
    Returns:
        Boolean: 密码是否正确
    """
    encrypted_input = md5_encrypt(input_password)
    return encrypted_input == stored_encrypted_password

def validate_email(email):
    """
    验证邮箱格式
    Args:
        email: 邮箱地址
    Returns:
        Boolean: 格式是否正确
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_client_ip(request):
    """
    获取客户端IP地址
    Args:
        request: Django request对象
    Returns:
        IP地址字符串
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class ResponseCode:
    """响应状态码常量类"""
    SUCCESS = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500