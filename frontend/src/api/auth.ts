import request from '@/utils/request'
import type { ApiResponse } from '@/types/api'
import type { LoginRequest, RegisterRequest, User, LoginResponse } from '@/types/auth'

// 用户登录
export function login(data: LoginRequest): Promise<ApiResponse<LoginResponse>> {
  return request({
    url: '/login/auth/login/',
    method: 'post',
    data,
  })
}

// 用户注册
export function register(data: RegisterRequest): Promise<ApiResponse<User>> {
  return request({
    url: '/login/auth/register/',
    method: 'post',
    data,
  })
}

// 获取用户信息
export function getUserInfo(): Promise<ApiResponse<User>> {
  return request({
    url: '/users/me/',
    method: 'get',
  })
}

// 刷新 token
export function refreshToken(): Promise<ApiResponse<{ token: string }>> {
  return request({
    url: '/auth/refresh/',
    method: 'post',
  })
}
