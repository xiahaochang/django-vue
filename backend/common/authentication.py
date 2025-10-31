import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from Login.models import User

class JWTAuthentication(authentication.BaseAuthentication):
    """
    JWT Token 认证类
    """
    
    def authenticate(self, request):
        # 从请求头获取 token
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        
        # 如果没有 Authorization 头，返回 None 让其他认证类处理
        if not auth_header:
            return None
        
        if not auth_header.startswith('Bearer '):
            return None
        
        token = auth_header[7:]  # 去掉 'Bearer ' 前缀
        
        try:
            # 验证 token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            
            if not user_id:
                raise AuthenticationFailed('无效的Token')
            
            # 获取用户
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise AuthenticationFailed('用户不存在')
            
            # 检查用户是否激活
            if not user.is_active:
                raise AuthenticationFailed('用户已被禁用')
            
            return (user, token)
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token已过期')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('无效的Token')
        except Exception as e:
            # 记录其他异常
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"JWT认证异常: {str(e)}")
            raise AuthenticationFailed('认证失败')