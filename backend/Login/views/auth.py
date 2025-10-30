from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils import timezone
from ..models import User
from ..serializers import LoginSerializer, RegisterSerializer
from common.utils import format_response, ResponseCode, generate_jwt_token

class LoginView(APIView):
    """登录视图"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = generate_jwt_token(user)
            
            # 更新最后登录时间
            user.last_login = timezone.now()
            user.save()
            
            user_data = {
                'id': str(user.id),
                'username': user.username,
                'email': user.email,
                'created_at': user.created_at.isoformat() if user.created_at else None,
            }
            
            return format_response(
                code=ResponseCode.SUCCESS,
                msg="登录成功",
                data={
                    'user': user_data,
                    'token': token,
                    'expires_in': 24 * 60 * 60  # 24小时，单位秒
                }
            )
        else:
            return format_response(
                code=ResponseCode.BAD_REQUEST,
                msg="登录失败",
                data=serializer.errors
            )

class RegisterView(APIView):
    """注册视图"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            user_data = {
                'id': str(user.id),
                'username': user.username,
                'email': user.email,
                'created_at': user.created_at.isoformat() if user.created_at else None,
            }
            
            return format_response(
                code=ResponseCode.CREATED,
                msg="用户注册成功",
                data=user_data
            )
        else:
            return format_response(
                code=ResponseCode.BAD_REQUEST,
                msg="注册失败",
                data=serializer.errors
            )