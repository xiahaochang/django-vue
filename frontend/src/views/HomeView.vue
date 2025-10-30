<template>
  <AppLayout>
    <div class="home-view">
      <el-card class="welcome-card">
        <template #header>
          <div class="card-header">
            <span class="header-title">系统首页</span>
          </div>
        </template>

        <div class="welcome-content">
          <el-icon :size="60" color="var(--success-color)" class="welcome-icon">
            <SuccessFilled />
          </el-icon>
          <h2 class="welcome-title">欢迎回来，{{ authStore.user?.username }}！</h2>
          <p class="welcome-description">您已成功登录 Vue 管理系统</p>

          <div class="user-info-card">
            <h3 class="info-title">用户信息</h3>
            <el-descriptions :column="1" border>
              <el-descriptions-item label="用户名">
                {{ authStore.user?.username }}
              </el-descriptions-item>
              <el-descriptions-item label="邮箱">
                {{ authStore.user?.email }}
              </el-descriptions-item>
              <el-descriptions-item label="账号状态">
                <el-tag :type="authStore.user?.is_active ? 'success' : 'danger'">
                  {{ authStore.user?.is_active ? '激活' : '禁用' }}
                </el-tag>
              </el-descriptions-item>
              <el-descriptions-item label="注册时间">
                {{ formatDate(authStore.user?.created_at) }}
              </el-descriptions-item>
              <el-descriptions-item label="最后登录" v-if="authStore.user?.last_login">
                {{ formatDate(authStore.user?.last_login) }}
              </el-descriptions-item>
            </el-descriptions>
          </div>
        </div>
      </el-card>
    </div>
  </AppLayout>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { SuccessFilled } from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth'
import AppLayout from '@/components/common/AppLayout.vue'

const authStore = useAuthStore()

const formatDate = (dateString?: string): string => {
  if (!dateString) return '未知'
  return new Date(dateString).toLocaleString('zh-CN')
}

onMounted(() => {
  // 确保用户信息已加载
  if (!authStore.user && authStore.token) {
    authStore.getUser()
  }
})
</script>

<style lang="scss" scoped>
.home-view {
  padding: 1rem;
}

.welcome-card {
  max-width: 800px;
  margin: 0 auto;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
}

.welcome-content {
  text-align: center;
  padding: 2rem 0;
}

.welcome-icon {
  margin-bottom: 1.5rem;
}

.welcome-title {
  margin: 1rem 0 0.5rem;
  color: var(--text-primary);
  font-size: 1.5rem;
}

.welcome-description {
  color: var(--text-regular);
  margin-bottom: 2rem;
  font-size: 1rem;
}

.user-info-card {
  text-align: left;
  background: var(--background-color);
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 2rem;
}

.info-title {
  margin-bottom: 1rem;
  color: var(--text-primary);
  font-size: 1.1rem;
  font-weight: 600;
}

:deep(.el-descriptions) {
  background: white;
  padding: 1rem;
  border-radius: 6px;
}

:deep(.el-descriptions__label) {
  font-weight: 500;
}
</style>
