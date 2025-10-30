// API 响应数据类型
export interface ApiResponse<T = any> {
  code: number
  msg: string
  data: T
}

export interface PaginatedResponse<T = any> {
  count: number
  total_pages: number
  current_page: number
  page_size: number
  has_next: boolean
  has_previous: boolean
  next_page: number | null
  previous_page: number | null
  results: T[]
}

export interface ListParams {
  page?: number
  page_size?: number
  search?: string
  ordering?: string
  [key: string]: any
}
