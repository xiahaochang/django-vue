import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { BabyRecord, Comment, User } from '@/types/babyTree'

export const useBabyTreeStore = defineStore('babyTree', () => {
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
      images: ['https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400'],
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
      images: ['https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=400'],
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
      ],
      recordBy: '妈妈',
      recordTime: '2024-02-05',
      createdAt: '2024-02-05 15:30:00',
      likes: 15,
      isLiked: true,
      tags: ['运动', '亲子活动'],
    },
  ])

  const comments = ref<Comment[]>([
    {
      id: '1',
      recordId: '1',
      userId: '2',
      userName: '爸爸',
      userAvatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100',
      content: '看到宝宝一天天成长，真的太幸福了！',
      createTime: '2024-01-15 15:00:00',
      likes: 3,
    },
    {
      id: '2',
      recordId: '1',
      userId: '3',
      userName: '奶奶',
      userAvatar: 'https://images.unsplash.com/photo-1551836026-d5cbc2f15155?w=100',
      content: '宝宝真棒！奶奶为你骄傲！',
      createTime: '2024-01-15 16:30:00',
      likes: 2,
    },
  ])

  const currentUser = ref<User>({
    id: '1',
    username: '妈妈',
    role: 'admin',
    avatar: 'https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100',
  })

  const addRecord = (record: Omit<BabyRecord, 'id' | 'createdAt' | 'likes' | 'isLiked'>) => {
    const newRecord: BabyRecord = {
      ...record,
      id: Date.now().toString(),
      createdAt: new Date().toISOString(),
      likes: 0,
      isLiked: false,
    }
    records.value.unshift(newRecord)
  }

  const updateRecord = (id: string, updates: Partial<BabyRecord>) => {
    const index = records.value.findIndex((record) => record.id === id)
    if (index !== -1) {
      records.value[index] = { ...records.value[index], ...updates }
    }
  }

  const deleteRecord = (id: string) => {
    records.value = records.value.filter((record) => record.id !== id)
  }

  const toggleLike = (id: string) => {
    const record = records.value.find((r) => r.id === id)
    if (record) {
      if (record.isLiked) {
        record.likes--
      } else {
        record.likes++
      }
      record.isLiked = !record.isLiked
    }
  }

  const addComment = (recordId: string, content: string) => {
    const newComment: Comment = {
      id: Date.now().toString(),
      recordId,
      userId: currentUser.value.id,
      userName: currentUser.value.username,
      userAvatar: currentUser.value.avatar,
      content,
      createTime: new Date().toISOString(),
      likes: 0,
    }
    comments.value.push(newComment)
  }

  return {
    records,
    comments,
    currentUser,
    addRecord,
    updateRecord,
    deleteRecord,
    toggleLike,
    addComment,
  }
})
