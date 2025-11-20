<template>
  <AppLayout>
    <div class="baby-tree-view">
      <!-- 页面标题和操作 -->
      <div class="page-header">
        <div class="header-content">
          <h1 class="page-title">留言板</h1>
          <p class="page-subtitle">把你相对宝宝说的话留在这里吧</p>
        </div>
        <button v-if="isAdmin" class="add-record-btn" @click="showAddDialog = true">
          <el-icon><Plus /></el-icon>
          添加记录
        </button>
      </div>
    </div>
  </AppLayout>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import { useBabyTreeStore } from '@/stores/babyTree'
import AppLayout from '@/components/common/AppLayout.vue'

const babyTreeStore = useBabyTreeStore()

const showAddDialog = ref(false)

const isAdmin = computed(() => babyTreeStore.currentUser.role === 'admin')

onMounted(() => {
  // 可以在这里加载数据
})
</script>

<style lang="scss" scoped>
.baby-tree-view {
  height: 100%;
  padding-bottom: 20px;
  overflow: hidden;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 225, 225, 0.5);
  height: 120px;

  .header-content {
    .page-title {
      margin: 0 0 8px 0;
      font-size: 32px;
      font-weight: 700;
      color: #ff6b6b;
      background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .page-subtitle {
      margin: 0;
      color: #ff8e8e;
      font-size: 16px;
    }
  }

  .add-record-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 24px;
    background: #ff6b6b;
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);

    &:hover {
      background: #ff5252;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }
  }
}

@media (max-width: 768px) {
  .page-header {
    gap: 16px;

    .page-title {
      font-size: 24px;
    }
  }
}
</style>
