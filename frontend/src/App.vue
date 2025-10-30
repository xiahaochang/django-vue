<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

onMounted(() => {
  // 应用启动时初始化认证状态
  authStore.initAuth()
})
</script>

<style lang="scss">
// 全局样式已经在 style.scss 中定义
</style>
