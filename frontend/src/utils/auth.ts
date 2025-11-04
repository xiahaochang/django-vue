// Token 管理工具函数
import type { User } from '@/types/auth'

const TOKEN_KEY = 'user_token'

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY)
}

export function setToken(token: string): void {
  localStorage.setItem(TOKEN_KEY, token)
}

export function removeToken(): void {
  localStorage.removeItem(TOKEN_KEY)
}

export function clearStorage(): void {
  localStorage.clear()
}

const USER_INFO = 'userInfo'

export function getUser(): string | null {
  return localStorage.getItem(USER_INFO)
}

export function setUser(token: User): void {
  localStorage.setItem(USER_INFO, JSON.stringify(token))
}

export function removeUser(): void {
  localStorage.removeItem(USER_INFO)
}
