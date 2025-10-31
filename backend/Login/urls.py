from django.urls import path
from .views import LoginView, RegisterView, UserListView, UserDetailView, UserUpdateView, CurrentUserView
from Login import views

urlpatterns = [
    # 认证相关
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    
    # 用户管理
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<uuid:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/me/', CurrentUserView.as_view(), name='current-user'),  # 新增当前用户接口

]