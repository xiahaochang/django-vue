<template>
  <div class="baby-tree-card" @click="handleClick">
    <!-- 图片区域 -->
    <div v-if="record.images.length > 0" class="card-images">
      <div
        v-for="(image, index) in record.images.slice(0, 3)"
        :key="index"
        :class="['image-item', { multiple: record.images.length > 1 }]"
      >
        <img :src="image" :alt="record.title" />
        <div v-if="index === 2 && record.images.length > 3" class="image-more">
          +{{ record.images.length - 3 }}
        </div>
      </div>
    </div>

    <!-- 内容区域 -->
    <div class="card-content">
      <h3 class="card-title">{{ record.title }}</h3>
      <p class="card-text">{{ record.content }}</p>

      <!-- 标签 -->
      <div v-if="record.tags.length > 0" class="card-tags">
        <span v-for="tag in record.tags" :key="tag" class="tag">
          {{ tag }}
        </span>
      </div>

      <!-- 元信息 -->
      <div class="card-meta">
        <div class="meta-left">
          <span class="record-by">{{ record.recordBy }}</span>
          <span class="record-time">{{ formatDate(record.recordTime) }}</span>
        </div>
        <div class="meta-right">
          <button class="like-btn" :class="{ liked: record.isLiked }" @click.stop="handleLike">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path
                d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
                :fill="record.isLiked ? '#ff6b6b' : 'none'"
                :stroke="record.isLiked ? '#ff6b6b' : '#999'"
                stroke-width="2"
              />
            </svg>
            {{ record.likes }}
          </button>
        </div>
      </div>

      <!-- 操作按钮（管理员显示） -->
      <div v-if="isAdmin" class="card-actions">
        <button class="action-btn edit-btn" @click.stop="handleEdit">编辑</button>
        <button class="action-btn delete-btn" @click.stop="handleDelete">删除</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { BabyRecord } from '@/types/babyTree'
import { useBabyTreeStore } from '@/stores/babyTree'

interface Props {
  record: BabyRecord
}

interface Emits {
  (e: 'click'): void
  (e: 'edit'): void
  (e: 'delete'): void
  (e: 'like'): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()
const babyTreeStore = useBabyTreeStore()

const isAdmin = computed(() => babyTreeStore.currentUser.role === 'admin')

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

const handleClick = () => {
  emit('click')
}

const handleEdit = () => {
  emit('edit')
}

const handleDelete = () => {
  emit('delete')
}

const handleLike = () => {
  emit('like')
}
</script>

<style lang="scss" scoped>
.baby-tree-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(255, 150, 150, 0.1);
  border: 1px solid rgba(255, 225, 225, 0.5);
  transition: all 0.3s ease;
  cursor: pointer;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(255, 150, 150, 0.15);
  }
}

.card-images {
  display: grid;
  //   grid-template-columns: repeat(3, 1fr);
  gap: 2px;
  height: 200px;

  .image-item {
    position: relative;
    overflow: hidden;

    &.multiple {
      &:first-child:nth-last-child(2),
      &:first-child:nth-last-child(2) ~ .image-item {
        grid-column: span 2;
      }
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }

    .image-more {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.6);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: 600;
    }
  }

  &:hover .image-item img {
    transform: scale(1.05);
  }
}

.card-content {
  padding: 20px;
}

.card-title {
  margin: 0 0 12px 0;
  font-size: 18px;
  font-weight: 600;
  color: #ff6b6b;
  line-height: 1.4;
}

.card-text {
  margin: 0 0 16px 0;
  color: #666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;

  .tag {
    padding: 4px 12px;
    background: rgba(255, 107, 107, 0.1);
    color: #ff6b6b;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 500;
  }
}

.card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 225, 225, 0.5);
}

.meta-left {
  display: flex;
  flex-direction: column;
  gap: 4px;

  .record-by {
    font-weight: 600;
    color: #ff6b6b;
    font-size: 14px;
  }

  .record-time {
    font-size: 12px;
    color: #999;
  }
}

.like-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: 1px solid rgba(255, 200, 200, 0.5);
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.8);
  color: #999;
  font-size: 12px;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    border-color: #ff6b6b;
    color: #ff6b6b;
    path {
      stroke: #ff6b6b;
    }
  }

  &.liked {
    border-color: #ff6b6b;
    background: rgba(255, 107, 107, 0.1);
    color: #ff6b6b;
  }
}

.card-actions {
  display: flex;
  gap: 8px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 225, 225, 0.3);

  .action-btn {
    flex: 1;
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;

    &.edit-btn {
      background: rgba(255, 193, 7, 0.1);
      color: #ff9800;

      &:hover {
        background: rgba(255, 193, 7, 0.2);
      }
    }

    &.delete-btn {
      background: rgba(244, 67, 54, 0.1);
      color: #f44336;

      &:hover {
        background: rgba(244, 67, 54, 0.2);
      }
    }
  }
}
</style>
