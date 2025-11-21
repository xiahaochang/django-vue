<template>
  <el-dialog v-model="visible" :title="record?.title" :before-close="handleClose">
    <!-- 内容区域 -->
    <div class="detail-content">
      <div class="detail-meta">
        <div class="meta-info">
          <span class="record-by">{{ record.content }}</span>
        </div>
      </div>
    </div>

    <!-- 操作按钮（管理员） -->
    <template #footer>
      <div class="detail-actions">
        <button class="action-btn edit-btn" @click="handleCancle">取消</button>
        <button class="action-btn delete-btn" @click="handleConfirm">确认</button>
      </div>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { ConfirmData } from '@/types/dataSource'

interface Props {
  modelValue: boolean
  record: ConfirmData
}

interface Emits {
  (e: 'update:modelValue', value: boolean): void
  (e: 'cancle', record: ConfirmData): void
  (e: 'confirm', record: ConfirmData): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const visible = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const handleClose = () => {
  visible.value = false
}

const handleCancle = () => {
  emit('cancle', props.record)
  handleClose()
}

const handleConfirm = async () => {
  emit('confirm', props.record)
  handleClose()
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
