from rest_framework.views import APIView
from common.utils import (
    md5_encrypt, 
    format_response, 
    generate_jwt_token, 
    verify_password,
    ResponseCode
)
from .models import User


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        
        if not username or not password or not email:
            return format_response(
                code=ResponseCode.BAD_REQUEST,
                msg="用户名、密码和邮箱均为必填字段",
                data=None
            )
        
        # 使用公共工具函数
        encrypted_password = md5_encrypt(password)
        
        try:
            user = User.objects.create(
                username=username,
                password=encrypted_password,
                email=email
            )
            
            return format_response(
                code=ResponseCode.CREATED,
                msg="用户注册成功",
                data={
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            )
        except Exception as e:
            return format_response(
                code=ResponseCode.INTERNAL_SERVER_ERROR,
                msg=f"注册失败: {str(e)}",
                data=None
            )


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(username=username)
            
            # 使用公共工具函数验证密码
            if not verify_password(password, user.password):
                return format_response(
                    code=ResponseCode.BAD_REQUEST,
                    msg="用户名或密码错误",
                    data=None
                )
            
            # 生成 JWT token
            token = generate_jwt_token(user)
            
            return format_response(
                code=ResponseCode.SUCCESS,
                msg="登录成功",
                data={
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email
                    },
                    'token': token
                }
            )
        except User.DoesNotExist:
            return format_response(
                code=ResponseCode.BAD_REQUEST,
                msg="用户名或密码错误",
                data=None
            )