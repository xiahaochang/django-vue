<template>
  <div class="loading-container" v-if="loading">
    <div class="loading-spinner">
      <el-icon class="is-loading spinner-icon">
        <Loading />
      </el-icon>
      <p class="loading-text">{{ text }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Loading } from '@element-plus/icons-vue'

interface Props {
  loading: boolean
  text?: string
}

withDefaults(defineProps<Props>(), {
  loading: false,
  text: '加载中...',
})
</script>

<style lang="scss" scoped>
.loading-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  backdrop-filter: blur(2px);
}

.loading-spinner {
  text-align: center;
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.spinner-icon {
  color: var(--primary-color);
  font-size: 2rem;
}

.loading-text {
  margin-top: 1rem;
  color: var(--text-regular);
  font-size: 0.9rem;
}
</style>
