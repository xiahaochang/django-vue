import { defineStore } from 'pinia'
import { ref } from 'vue'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { login, register, getUserInfo } from '@/api/auth'
import type { LoginRequest, RegisterRequest, User, AuthState } from '@/types/auth'

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string>(getToken() || '')
  const user = ref<User | null>(null)
  const isLoggedIn = ref<boolean>(!!getToken())

  // 登录
  const userLogin = async (loginData: LoginRequest): Promise<any> => {
    try {
      const response = await login(loginData)
      const { token: userToken, user: userInfo } = response.data

      token.value = userToken
      user.value = userInfo
      isLoggedIn.value = true
      setToken(userToken)

      return response.data
    } catch (error) {
      return Promise.reject(error)
    }
  }

  // 注册
  const userRegister = async (registerData: RegisterRequest): Promise<any> => {
    try {
      const response = await register(registerData)
      return response.data
    } catch (error) {
      return Promise.reject(error)
    }
  }

  // 获取用户信息
  const getUser = async (): Promise<User> => {
    try {
      const response = await getUserInfo()
      user.value = response.data
      return response.data
    } catch (error) {
      return Promise.reject(error)
    }
  }

  // 退出登录
  const logout = (): void => {
    token.value = ''
    user.value = null
    isLoggedIn.value = false
    removeToken()
  }

  // 初始化认证状态
  const initAuth = async (): Promise<void> => {
    if (token.value) {
      try {
        await getUser()
      } catch (error) {
        logout()
      }
    }
  }

  return {
    token,
    user,
    isLoggedIn,
    userLogin,
    userRegister,
    getUser,
    logout,
    initAuth,
  }
})
