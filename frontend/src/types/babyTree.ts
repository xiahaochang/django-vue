export interface BabyRecord {
  id: string
  title: string
  content: string
  images: string[]
  recordBy: string
  recordTime: string
  createdAt: string
  likes: number
  isLiked: boolean
  tags: string[]
}

export interface Comment {
  id: string
  recordId: string
  userId: string
  userName: string
  userAvatar: string
  content: string
  createTime: string
  likes: number
}

export interface User {
  id: string
  username: string
  role: 'admin' | 'user'
  avatar: string
}
