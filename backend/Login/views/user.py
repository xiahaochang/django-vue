from rest_framework.views import APIView
from common.authentication import JWTAuthentication
from common.utils import (
    format_response, 
    ResponseCode
)
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from django.db.models import Q
from ..models import User
from ..serializers import UserListSerializer, UserDetailSerializer, UserUpdateSerializer, CurrentUserSerializer
from common.pagination import StandardPagination
from ..permissions import IsAdminOrReadOnly, UserProfilePermission
from rest_framework.permissions import IsAuthenticated


class UserListView(ListAPIView):
    """用户列表分页接口"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # 获取查询参数
        search = self.request.query_params.get('search', '')
        is_active = self.request.query_params.get('is_active', '')
        ordering = self.request.query_params.get('ordering', '-created_at')
        
        # 搜索功能
        if search:
            queryset = queryset.filter(
                Q(username__icontains=search) | 
                Q(email__icontains=search)
            )
        
        # 状态筛选
        if is_active.lower() in ['true', 'false']:
            is_active_bool = is_active.lower() == 'true'
            queryset = queryset.filter(is_active=is_active_bool)
        
        # 排序
        if ordering:
            allowed_ordering_fields = ['username', 'email', 'created_at', 'updated_at']
            if ordering.lstrip('-') in allowed_ordering_fields:
                queryset = queryset.order_by(ordering)
        
        return queryset

class UserDetailView(RetrieveAPIView):
    """用户详情接口"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [UserProfilePermission]

class UserUpdateView(UpdateAPIView):
    """用户更新接口"""
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [UserProfilePermission]
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return format_response(
            code=ResponseCode.SUCCESS,
            msg="用户信息更新成功",
            data=response.data
        )

class CurrentUserView(APIView):
    """获取当前登录用户信息"""
    authentication_classes = [JWTAuthentication]  # 使用JWT认证
    # permission_classes = [IsAuthenticated]  # 要求登录
    
    def get(self, request):
        """获取当前用户信息"""
        user = request.user
        
        return format_response(
            code=ResponseCode.SUCCESS,
            msg="获取用户信息成功",
            data={
                'id': str(user.id),
                'username': user.username,
                'email': user.email,
                'is_active': user.is_active,
                'created_at': user.created_at.isoformat() if user.created_at else None
            }
        )
        
