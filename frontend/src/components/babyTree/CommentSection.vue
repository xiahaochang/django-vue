<template>
  <div class="comment-section">
    <h3 class="comment-title">评论 ({{ comments.length }})</h3>

    <!-- 评论列表 -->
    <div class="comment-list">
      <div v-for="comment in comments" :key="comment.id" class="comment-item">
        <div class="comment-avatar">
          <img :src="comment.userAvatar" :alt="comment.userName" />
        </div>
        <div class="comment-content">
          <div class="comment-header">
            <span class="user-name">{{ comment.userName }}</span>
            <span class="comment-time">{{ formatTime(comment.createTime) }}</span>
          </div>
          <p class="comment-text">{{ comment.content }}</p>
        </div>
      </div>
    </div>

    <!-- 添加评论 -->
    <div class="add-comment">
      <div class="comment-avatar">
        <img :src="currentUser.avatar" :alt="currentUser.username" />
      </div>
      <div class="comment-input-wrapper">
        <textarea
          v-model="newComment"
          placeholder="写下你的祝福和评论..."
          class="comment-input"
          rows="3"
        ></textarea>
        <button class="submit-btn" :disabled="!newComment.trim()" @click="handleSubmit">
          发布评论
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Comment } from '@/types/babyTree'
import { useBabyTreeStore } from '@/stores/babyTree'

interface Props {
  recordId: string
  comments: Comment[]
}

interface Emits {
  (e: 'commentAdded', content: string): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()
const babyTreeStore = useBabyTreeStore()

const newComment = ref('')
const { currentUser } = babyTreeStore

const formatTime = (timeString: string) => {
  const date = new Date(timeString)
  const now = new Date()
  const diff = now.getTime() - date.getTime()

  if (diff < 60000) return '刚刚'
  if (diff < 3600000) return `${Math.floor(diff / 60000)}分钟前`
  if (diff < 86400000) return `${Math.floor(diff / 3600000)}小时前`

  return date.toLocaleDateString('zh-CN', {
    month: 'short',
    day: 'numeric',
  })
}

const handleSubmit = () => {
  if (newComment.value.trim()) {
    emit('commentAdded', newComment.value.trim())
    newComment.value = ''
  }
}
</script>

<style lang="scss" scoped>
.comment-section {
  padding: 24px 0;
}

.comment-title {
  margin: 0 0 20px 0;
  font-size: 18px;
  font-weight: 600;
  color: #ff6b6b;
}

.comment-list {
  margin-bottom: 24px;
}

.comment-item {
  display: flex;
  gap: 12px;
  padding: 16px 0;
  border-bottom: 1px solid rgba(255, 225, 225, 0.5);

  &:last-child {
    border-bottom: none;
  }
}

.comment-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

.comment-content {
  flex: 1;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;

  .user-name {
    font-weight: 600;
    color: #ff6b6b;
    font-size: 14px;
  }

  .comment-time {
    font-size: 12px;
    color: #999;
  }
}

.comment-text {
  margin: 0;
  color: #666;
  line-height: 1.5;
  font-size: 14px;
}

.add-comment {
  display: flex;
  gap: 12px;
  padding: 20px;
  background: rgba(255, 250, 250, 0.8);
  border-radius: 12px;
  border: 1px solid rgba(255, 225, 225, 0.5);
}

.comment-input-wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.comment-input {
  width: 100%;
  padding: 12px;
  border: 1px solid rgba(255, 200, 200, 0.5);
  border-radius: 8px;
  background: white;
  resize: vertical;
  font-family: inherit;
  font-size: 14px;
  transition: border-color 0.3s ease;

  &:focus {
    outline: none;
    border-color: #ff6b6b;
  }

  &::placeholder {
    color: #ccc;
  }
}

.submit-btn {
  align-self: flex-end;
  padding: 8px 20px;
  background: #ff6b6b;
  color: white;
  border: none;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover:not(:disabled) {
    background: #ff5252;
    transform: translateY(-1px);
  }

  &:disabled {
    background: #ccc;
    cursor: not-allowed;
    transform: none;
  }
}
</style>
