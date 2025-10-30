// 认证相关类型定义
export interface User {
  id: string
  username: string
  email: string
  is_active: boolean
  created_at: string
  updated_at?: string
  last_login?: string
}

export interface LoginRequest {
  username: string
  password: string
}

export interface RegisterRequest {
  username: string
  email: string
  password: string
  password_confirm: string
}

export interface LoginResponse {
  user: User
  token: string
  expires_in: number
}

export interface AuthState {
  token: string
  user: User | null
  isLoggedIn: boolean
}
