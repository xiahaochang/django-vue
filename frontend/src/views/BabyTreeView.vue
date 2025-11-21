<template>
  <AppLayout>
    <div class="baby-tree-view" ref="scrollContainer">
      <!-- 页面标题和操作 -->
      <div class="page-header">
        <div class="header-content">
          <h1 class="page-title">宝贝成长树</h1>
          <p class="page-subtitle">记录宝宝成长的每一个珍贵瞬间</p>
        </div>
        <button v-if="isAdmin" class="add-record-btn" @click="showAddDialog = true">
          <el-icon><Plus /></el-icon>
          添加记录
        </button>
      </div>

      <!-- 瀑布流展示 -->
      <div class="waterfall-wrapper">
        <BabyTreeWaterfall
          :records="records"
          @card-click="handleCardClick"
          @edit="handleEdit"
          @delete="handleDelete"
          @like="handleLike"
        />
      </div>

      <!-- 添加/编辑记录弹窗 -->
      <el-dialog v-model="showAddDialog" :title="editingRecord ? '编辑成长记录' : '添加成长记录'">
        <el-form :model="recordForm" :rules="formRules" ref="formRef" label-width="80px">
          <el-form-item label="标题" prop="title">
            <el-input v-model="recordForm.title" placeholder="请输入记录标题" />
          </el-form-item>
          <el-form-item label="内容" prop="content">
            <el-input
              v-model="recordForm.content"
              type="textarea"
              :rows="4"
              placeholder="记录下这个珍贵的时刻..."
            />
          </el-form-item>
          <el-form-item label="记录时间" prop="recordTime">
            <el-date-picker
              v-model="recordForm.recordTime"
              type="date"
              placeholder="选择日期"
              value-format="YYYY-MM-DD"
            />
          </el-form-item>
          <el-form-item label="照片" prop="images">
            <div class="upload-container">
              <el-upload
                v-model:file-list="recordForm.images"
                action="#"
                list-type="picture-card"
                :auto-upload="false"
                :multiple="true"
                :limit="9"
                :on-exceed="handleExceed"
                :on-change="handleImageChange"
                :on-remove="handleImageRemove"
              >
                <el-icon><Plus /></el-icon>
              </el-upload>
            </div>
          </el-form-item>
          <el-form-item label="标签">
            <el-select
              v-model="recordForm.tags"
              multiple
              placeholder="选择标签"
              style="width: 100%"
            >
              <el-option v-for="tag in availableTags" :key="tag" :label="tag" :value="tag" />
            </el-select>
          </el-form-item>
        </el-form>

        <template #footer>
          <el-button @click="showAddDialog = false">取消</el-button>
          <el-button type="primary" @click="handleSaveRecord">
            {{ editingRecord ? '更新' : '保存' }}
          </el-button>
        </template>
      </el-dialog>

      <!-- 记录详情弹窗 -->
      <BabyTreeDetail
        v-model="showDetail"
        :record="selectedRecord!"
        @edit="handleEdit"
        @delete="handleDelete"
        @like="handleLike"
        @comment-added="handleCommentAdded"
      />

      <!-- 自定义悬浮功能按钮组 -->
      <div class="floating-action-group" :class="{ expanded: isExpanded }">
        <!-- 主按钮 -->
        <button class="fab-main" @click="toggleExpand">
          <el-icon v-if="!isExpanded"><Plus /></el-icon>
          <el-icon v-else><Close /></el-icon>
        </button>

        <!-- 功能按钮 -->
        <div class="fab-actions" v-if="isExpanded">
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
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue'
import {
  ElMessage,
  ElMessageBox,
  type FormInstance,
  type FormRules,
  type UploadFile,
} from 'element-plus'
import { Plus, Close, Top, Edit } from '@element-plus/icons-vue'
import type { BabyRecord } from '@/types/babyTree'
import { useBabyTreeStore } from '@/stores/babyTree'
import BabyTreeWaterfall from '@/components/babyTree/BabyTreeWaterfall.vue'
import BabyTreeDetail from '@/components/babyTree/BabyTreeDetail.vue'
import AppLayout from '@/components/common/AppLayout.vue'

const babyTreeStore = useBabyTreeStore()
const formRef = ref<FormInstance>()

const showAddDialog = ref(false)
const showDetail = ref(false)
const editingRecord = ref<BabyRecord | null>(null)
const selectedRecord = ref<BabyRecord | null>(null)

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

const availableTags = [
  '里程碑',
  '运动发展',
  '语言发展',
  '饮食',
  '健康',
  '亲子活动',
  '感人时刻',
  '第一次',
  '重要里程碑',
]

const records = ref<BabyRecord[]>([
  {
    id: '1',
    title: '第一次翻身',
    content:
      '今天宝宝第一次自己翻身了！虽然动作还不太熟练，但是看到她努力的样子，爸爸妈妈都好感动。',
    images: [
      'https://images.unsplash.com/photo-1511895426328-dc8714191300?w=400',
      'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400',
    ],
    recordBy: '妈妈',
    recordTime: '2024-01-15',
    createdAt: '2024-01-15 14:30:00',
    likes: 12,
    isLiked: false,
    tags: ['里程碑', '运动发展'],
  },
  {
    id: '2',
    title: '第一次叫妈妈',
    content: '今天是个特别的日子！宝宝第一次清晰地叫出了"妈妈"，那一刻我的心都要融化了。',
    images: ['https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=400'],
    recordBy: '爸爸',
    recordTime: '2024-02-20',
    createdAt: '2024-02-20 09:15:00',
    likes: 25,
    isLiked: true,
    tags: ['语言发展', '感人时刻'],
  },
  {
    id: '3',
    title: '第一次独立走路',
    content: '宝宝今天迈出了人生的第一步！虽然摇摇晃晃的，但是非常勇敢。',
    images: [
      'https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=400',
      'https://images.unsplash.com/photo-1544717305-2782549b5136?w=400',
      'https://images.unsplash.com/photo-1544717305-2782549b5136?w=400',
    ],
    recordBy: '妈妈',
    recordTime: '2024-03-10',
    createdAt: '2024-03-10 16:45:00',
    likes: 18,
    isLiked: false,
    tags: ['重要里程碑', '运动发展'],
  },
  {
    id: '4',
    title: '第一次吃辅食',
    content: '今天尝试给宝宝添加辅食，她好像很喜欢米粉的味道，吃得津津有味。',
    images: [
      'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=400',
      'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=400',
      'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=400',
      'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=400',
    ],
    recordBy: '爸爸',
    recordTime: '2024-01-28',
    createdAt: '2024-01-28 11:20:00',
    likes: 8,
    isLiked: false,
    tags: ['饮食', '成长'],
  },
  {
    id: '5',
    title: '第一次游泳',
    content: '带宝宝去游泳，她一点都不怕水，在水里玩得很开心，像只快乐的小鸭子。',
    images: [
      'https://images.unsplash.com/photo-1536599424071-0b215a388ba7?w=400',
      'https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=400',
      'https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=400',
      'https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=400',
      'https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=400',
    ],
    recordBy: '妈妈',
    recordTime: '2024-02-05',
    createdAt: '2024-02-05 15:30:00',
    likes: 15,
    isLiked: true,
    tags: ['运动', '亲子活动'],
  },
])

const recordForm = reactive({
  title: '',
  content: '',
  recordTime: '',
  tags: [] as string[],
  images: [] as UploadFile[],
})

// 表单验证规则
const formRules: FormRules = {
  title: [{ required: true, message: '请输入记录标题', trigger: 'blur' }],
  content: [{ required: true, message: '请输入记录内容', trigger: 'blur' }],
  recordTime: [{ required: true, message: '请选择记录时间', trigger: 'change' }],
  images: [
    {
      validator: (_, value, callback) => {
        if (!value || value.length === 0) {
          callback(new Error('请至少上传一张照片'))
        } else {
          callback()
        }
      },
      trigger: 'change',
    },
  ],
}

const isAdmin = computed(() => babyTreeStore.currentUser.role === 'admin')

const handleCardClick = (record: BabyRecord) => {
  selectedRecord.value = record
  showDetail.value = true
}

const handleEdit = (record: BabyRecord) => {
  editingRecord.value = record
  Object.assign(recordForm, {
    title: record.title,
    content: record.content,
    recordTime: record.recordTime,
    tags: [...record.tags],
    images: record.images.map((url) => ({ url, name: url, status: 'success' })),
  })
  showAddDialog.value = true
}

const handleDelete = async (record: BabyRecord) => {
  try {
    await ElMessageBox.confirm('确定要删除这条成长记录吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    })
    babyTreeStore.deleteRecord(record.id)
    ElMessage.success('删除成功')
  } catch {
    // 用户取消操作
  }
}

const handleLike = (id: string) => {
  babyTreeStore.toggleLike(id)
}

const handleCommentAdded = (recordId: string, content: string) => {
  babyTreeStore.addComment(recordId, content)
  ElMessage.success('评论发布成功')
}

// 图片上传处理
const handleImageChange = (file: UploadFile) => {
  if (file.raw) {
    const isImage = file.raw.type.startsWith('image/')
    const isLt2M = file.raw.size / 1024 / 1024 < 20

    if (!isImage) {
      ElMessage.error('只能上传图片文件')
      return false
    }
    if (!isLt2M) {
      ElMessage.error('图片大小不能超过 20MB')
      return false
    }
  }
  return true
}

const handleExceed = () => {
  ElMessage.warning('最多只能上传9张照片')
}

const handleImageRemove = () => {
  // 图片删除后的处理
}

const handleSaveRecord = async () => {
  if (!formRef.value) return

  try {
    await formRef.value.validate()

    if (editingRecord.value) {
      babyTreeStore.updateRecord(editingRecord.value.id, {
        ...recordForm,
        images: recordForm.images.map((file) => file.url || ''),
        recordBy: babyTreeStore.currentUser.username,
      })
      ElMessage.success('更新成功')
    } else {
      babyTreeStore.addRecord({
        ...recordForm,
        images: recordForm.images.map((file) => file.url || ''),
        recordBy: babyTreeStore.currentUser.username,
      })
      ElMessage.success('添加成功')
    }

    showAddDialog.value = false
    resetForm()
  } catch (error) {
    // 验证失败，不执行保存操作
  }
}

const resetForm = () => {
  editingRecord.value = null
  formRef.value?.clearValidate()
  Object.assign(recordForm, {
    title: '',
    content: '',
    recordTime: '',
    tags: [],
    images: [],
  })
}

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
