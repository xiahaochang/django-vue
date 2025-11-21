<template>
  <AppLayout>
    <div class="baby-tree-view" ref="scrollContainer">
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

      <!-- 自定义悬浮功能按钮组 -->
      <div class="floating-action-group" :class="{ expanded: isExpanded }">
        <!-- 主按钮 -->
        <button class="fab-main" @click="toggleExpand">
          <el-icon v-if="!isExpanded"><Plus /></el-icon>
          <el-icon v-else><Close /></el-icon>
        </button>

        <!-- 功能按钮 -->
        <div class="fab-actions">
          <!-- 回到顶部按钮 -->
          <button class="fab-action" @click="scrollToTop" title="回到顶部">
            <el-icon><Top /></el-icon>
          </button>

          <!-- 添加记录按钮 (仅管理员可见) -->
          <button v-if="isAdmin" class="fab-action" @click="showAddDialog = true" title="添加记录">
            <el-icon><Plus /></el-icon>
          </button>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import { Plus, Close, Top } from '@element-plus/icons-vue'
import { useBabyTreeStore } from '@/stores/babyTree'
import AppLayout from '@/components/common/AppLayout.vue'

const babyTreeStore = useBabyTreeStore()
const showAddDialog = ref(false)

const isExpanded = ref(false)
// 切换展开状态
const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}
// 回到顶部
const scrollContainer = ref<HTMLElement>()
const scrollToTop = () => {
  if (scrollContainer.value) {
    scrollContainer.value.scrollTo({
      top: 0,
      behavior: 'smooth',
    })
  }
  // 收起按钮组
  isExpanded.value = false
}

const isAdmin = computed(() => babyTreeStore.currentUser.role === 'admin')

onMounted(() => {})
</script>

<style lang="scss" scoped>
.baby-tree-view {
  height: 100%;
  padding-bottom: 20px;
  padding-right: 8px;
  overflow-y: auto;
  // overflow: hidden;
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

.waterfall-wrapper {
  padding: 10px 10px;
  // height: calc(100% - 100px);
  // overflow: hidden auto;
}

// 上传图片样式调整
.upload-container {
  :deep(.el-upload-list__item) {
    width: 100px;
    height: 100px;
  }

  :deep(.el-upload) {
    width: 100px;
    height: 100px;
    line-height: 100px;
  }
}

.upload-tip {
  margin-top: 8px;
  color: #999;
  font-size: 12px;
}

@media (max-width: 768px) {
  .page-header {
    gap: 16px;

    .page-title {
      font-size: 24px;
    }
  }
}

// 悬浮按钮组样式
.floating-action-group {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 1000;
  display: flex;
  flex-direction: column-reverse;
  align-items: center;
  gap: 12px;
  transition: all 0.3s ease;

  // 主按钮
  .fab-main {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
    transition: all 0.3s ease;
    z-index: 1001;

    &:hover {
      background: linear-gradient(135deg, #ff5252 0%, #ff7b7b 100%);
      transform: scale(1.05);
      box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }

    &:active {
      transform: scale(0.95);
    }
  }

  // 功能按钮容器
  .fab-actions {
    display: flex;
    flex-direction: column-reverse;
    gap: 12px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(20px);
    transition: all 0.3s ease;

    // 功能按钮
    .fab-action {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: white;
      border: 2px solid #ff6b6b;
      color: #ff6b6b;
      font-size: 18px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(255, 107, 107, 0.2);
      transition: all 0.3s ease;
      position: relative;

      &:hover {
        background: #ff6b6b;
        color: white;
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);

        // 悬停提示
        &::after {
          content: attr(title);
          position: absolute;
          right: 100%;
          top: 50%;
          transform: translateY(-50%);
          background: #ff6b6b;
          color: white;
          padding: 6px 12px;
          border-radius: 4px;
          font-size: 14px;
          white-space: nowrap;
          margin-right: 8px;
          pointer-events: none;
        }
      }

      &:active {
        transform: scale(0.95);
      }
    }
  }

  // 展开状态
  &.expanded {
    .fab-actions {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }

    .fab-main {
      background: linear-gradient(135deg, #ff5252 0%, #ff7b7b 100%);
    }
  }
}

// 响应式调整
@media (max-width: 768px) {
  .floating-action-group {
    right: 16px;
    bottom: 16px;

    .fab-main {
      width: 32px;
      height: 32px;
      font-size: 18px;
    }

    .fab-action {
      width: 32px;
      height: 32px;
      font-size: 16px;
    }
  }
}

// 平板设备调整
@media (max-width: 1024px) and (min-width: 769px) {
  .floating-action-group {
    right: 24px;
    bottom: 24px;
  }
}
</style>
