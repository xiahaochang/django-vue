<template>
  <div class="register-view">
    <div class="register-container">
      <div class="register-form-wrapper">
        <div class="register-header">
          <h1 class="register-title">用户注册</h1>
          <p class="register-subtitle">创建您的 Vue 管理系统账户</p>
        </div>

        <el-form
          ref="registerFormRef"
          :model="registerForm"
          :rules="registerRules"
          class="register-form"
          size="large"
        >
          <el-form-item prop="username">
            <el-input
              v-model="registerForm.username"
              placeholder="请输入用户名"
              :prefix-icon="User"
            />
          </el-form-item>

          <el-form-item prop="email">
            <el-input
              v-model="registerForm.email"
              placeholder="请输入邮箱地址"
              :prefix-icon="Message"
            />
          </el-form-item>

          <el-form-item prop="password">
            <el-input
              v-model="registerForm.password"
              type="password"
              placeholder="请输入密码"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>

          <el-form-item prop="password_confirm">
            <el-input
              v-model="registerForm.password_confirm"
              type="password"
              placeholder="请再次输入密码"
              :prefix-icon="Lock"
              show-password
            />
          </el-form-item>

          <el-form-item>
            <el-button
              type="primary"
              :loading="loading"
              @click="handleRegister"
              class="register-button"
            >
              {{ loading ? '注册中...' : '注册' }}
            </el-button>
          </el-form-item>
        </el-form>

        <div class="register-footer">
          <p class="login-link">
            已有账号？
            <router-link to="/login" class="link">立即登录</router-link>
          </p>
        </div>
      </div>
    </div>

    <LoadingSpinner :loading="loading" text="注册中..." />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, type FormInstance, type FormRules } from 'element-plus'
import { User, Message, Lock } from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth'
import { registerRules, validatePasswordConfirm } from '@/utils/validation'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import type { RegisterRequest } from '@/types/auth'

const router = useRouter()
const authStore = useAuthStore()

const registerFormRef = ref<FormInstance>()
const loading = ref<boolean>(false)

const registerForm = reactive<RegisterRequest>({
  username: '',
  email: '',
  password: '',
  password_confirm: '',
})

// 动态验证规则
const dynamicRegisterRules = computed<FormRules>(() => ({
  username: registerRules.username,
  email: registerRules.email,
  password: registerRules.password,
  password_confirm: [
    ...registerRules.password_confirm!,
    { validator: validatePasswordConfirm(registerForm.password), trigger: 'blur' },
  ],
}))

const handleRegister = async (): Promise<void> => {
  if (!registerFormRef.value) return

  try {
    const valid = await registerFormRef.value.validate()
    if (valid) {
      loading.value = true
      await authStore.userRegister(registerForm)
      ElMessage.success('注册成功！请登录')
      router.push('/login')
    }
  } catch (error: any) {
    console.error('注册失败:', error)
    // 错误信息已经在拦截器中显示
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  // 如果已登录，跳转到首页
  if (authStore.isLoggedIn) {
    router.push('/')
  }
})
</script>

<style lang="scss" scoped>
.register-view {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem;
}

.register-container {
  width: 100%;
  max-width: 450px;
}

.register-form-wrapper {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.register-header {
  text-align: center;
  margin-bottom: 2rem;
}

.register-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 0.5rem;
}

.register-subtitle {
  color: var(--text-regular);
  margin: 0;
  font-size: 0.9rem;
}

.register-form {
  .el-form-item {
    margin-bottom: 1.5rem;
  }
}

.register-button {
  width: 100%;
  height: 48px;
  font-size: 1rem;
  font-weight: 500;
}

.register-footer {
  text-align: center;
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
}

.login-link {
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
  .register-form-wrapper {
    padding: 2rem 1.5rem;
  }

  .register-title {
    font-size: 1.5rem;
  }
}
</style>
