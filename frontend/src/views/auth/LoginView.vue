<template>
  <div class="login-view">
    <div class="login-container">
      <div class="login-form-wrapper">
        <div class="login-header">
          <h1 class="login-title">用户登录</h1>
          <p class="login-subtitle">欢迎回到 Vue 管理系统</p>
        </div>

        <el-form
          ref="loginFormRef"
          :model="loginForm"
          :rules="loginRules"
          class="login-form"
          size="large"
        >
          <el-form-item prop="username">
            <el-input
              v-model="loginForm.username"
              placeholder="请输入用户名"
              :prefix-icon="User"
              @keyup.enter="handleLogin"
            />
          </el-form-item>

          <el-form-item prop="password">
            <el-input
              v-model="loginForm.password"
              type="password"
              placeholder="请输入密码"
              :prefix-icon="Lock"
              show-password
              @keyup.enter="handleLogin"
            />
          </el-form-item>

          <el-form-item>
            <el-button type="primary" :loading="loading" @click="handleLogin" class="login-button">
              {{ loading ? '登录中...' : '登录' }}
            </el-button>
          </el-form-item>
        </el-form>

        <div class="login-footer">
          <p class="register-link">
            还没有账号？
            <router-link to="/register" class="link">立即注册</router-link>
          </p>
        </div>
      </div>
    </div>

    <LoadingSpinner :loading="loading" text="登录中..." />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'
import { User, Lock } from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth'
import { loginRules } from '@/utils/validation'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import type { LoginRequest } from '@/types/auth'

const router = useRouter()
const authStore = useAuthStore()

const loginFormRef = ref<FormInstance>()
const loading = ref<boolean>(false)

const loginForm = reactive<LoginRequest>({
  username: 'testuser',
  password: '123456',
})

const handleLogin = async (): Promise<void> => {
  router.push('/')
  if (!loginFormRef.value) return

  // try {
  //   const valid = await loginFormRef.value.validate()
  //   if (valid) {
  //     loading.value = true
  //     await authStore.userLogin(loginForm)
  //     router.push('/')
  //   }
  // } catch (error: any) {
  //   console.error('登录失败:', error)
  //   // 错误信息已经在拦截器中显示
  // } finally {
  //   loading.value = false
  // }
}

onMounted(() => {
  // 如果已登录，跳转到首页
  if (authStore.isLoggedIn) {
    router.push('/')
  }
})
</script>

<style lang="scss" scoped>
.login-view {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem;
}

.login-container {
  width: 100%;
  max-width: 400px;
}

.login-form-wrapper {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.login-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem;
}

.login-subtitle {
  color: var(--text-regular);
  margin: 0;
  font-size: 0.9rem;
}

.login-form {
  .el-form-item {
    margin-bottom: 1.5rem;
  }
}

.login-button {
  width: 100%;
  height: 48px;
  font-size: 1rem;
  font-weight: 500;
}

.login-footer {
  text-align: center;
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
}

.register-link {
  margin: 0;
  color: var(--text-regular);
  font-size: 0.9rem;
}

.link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;

  &:hover {
    text-decoration: underline;
  }
}

// 响应式设计
@media (max-width: 480px) {
  .login-form-wrapper {
    padding: 2rem 1.5rem;
  }

  .login-title {
    font-size: 1.5rem;
  }
}
</style>
