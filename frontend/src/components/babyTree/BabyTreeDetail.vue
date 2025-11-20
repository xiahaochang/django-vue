<template>
  <el-dialog v-model="visible" :title="record?.title" fullscreen :before-close="handleClose">
    <!-- 图片展示 -->
    <div v-if="record.images.length > 0" class="detail-images">
      <el-carousel
        v-if="record.images.length > 1"
        arrow="always"
        height="400px"
        type="card"
        :autoplay="false"
      >
        <el-carousel-item v-for="image in record.images" :key="image">
          <img class="carousel-image" :src="image" :alt="record.title" />
        </el-carousel-item>
      </el-carousel>
      <img v-else :src="record.images[0]" :alt="record.title" class="single-image" />
    </div>

    <!-- 内容区域 -->
    <div class="detail-content">
      <div class="detail-meta">
        <div class="meta-info">
          <span class="record-by">记录人：{{ record.recordBy }}</span>
          <span class="record-time">时间：{{ formatDate(record.recordTime) }}</span>
        </div>
        <button
          class="like-btn detail-like"
          :class="{ liked: record.isLiked }"
          @click.stop="handleLike"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
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

      <p class="detail-text">{{ record.content }}</p>

      <!-- 标签 -->
      <div v-if="record.tags.length > 0" class="detail-tags">
        <span v-for="tag in record.tags" :key="tag" class="tag">
          {{ tag }}
        </span>
      </div>
    </div>

    <!-- 评论区域 -->
    <CommentSection
      :record-id="record.id"
      :comments="recordComments"
      @comment-added="handleCommentAdded"
    />

    <!-- 操作按钮（管理员） -->
    <template #footer v-if="isAdmin">
      <div class="detail-actions">
        <button class="action-btn edit-btn" @click="handleEdit">编辑记录</button>
        <button class="action-btn delete-btn" @click="handleDelete">删除记录</button>
      </div>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { ElMessageBox } from 'element-plus'
import type { BabyRecord, Comment } from '@/types/babyTree'
import { useBabyTreeStore } from '@/stores/babyTree'
import CommentSection from './CommentSection.vue'

interface Props {
  modelValue: boolean
  record: BabyRecord
}

interface Emits {
  (e: 'update:modelValue', value: boolean): void
  (e: 'edit', record: BabyRecord): void
  (e: 'delete', record: BabyRecord): void
  (e: 'like', id: string): void
  (e: 'comment-added', recordId: string, content: string): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()
const babyTreeStore = useBabyTreeStore()

const visible = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const isAdmin = computed(() => babyTreeStore.currentUser.role === 'admin')

const recordComments = computed(() => {
  return babyTreeStore.comments.filter((comment) => comment.recordId === props.record.id)
})

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

const handleClose = () => {
  visible.value = false
}

const handleEdit = () => {
  emit('edit', props.record)
  handleClose()
}

const handleDelete = async () => {
  try {
    await ElMessageBox.confirm('确定要删除这条成长记录吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    })
    emit('delete', props.record)
    handleClose()
  } catch {
    // 用户取消操作
  }
}

const handleLike = () => {
  emit('like', props.record.id)
}

const handleCommentAdded = (content: string) => {
  emit('comment-added', props.record.id, content)
}
</script>

<style lang="scss" scoped>
.detail-images {
  margin-bottom: 24px;
  border-radius: 12px;
  overflow: hidden;

  .carousel-image,
  .single-image {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
}

.detail-content {
  padding: 0 0 24px;
}

.detail-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 225, 225, 0.5);
}

.meta-info {
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

.detail-like {
  padding: 8px 16px;
  font-size: 14px;
}

.detail-text {
  margin: 0 0 16px 0;
  color: #666;
  line-height: 1.8;
  font-size: 15px;
}

.detail-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;

  .tag {
    padding: 6px 12px;
    background: rgba(255, 107, 107, 0.1);
    color: #ff6b6b;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 500;
  }
}

.detail-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;

  .action-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
    font-size: 14px;
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
