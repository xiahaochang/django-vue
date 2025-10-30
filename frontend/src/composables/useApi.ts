import { ref } from 'vue'
import type { Ref } from 'vue'
import { ElMessage } from 'element-plus'

interface UseApiOptions {
  showLoading?: boolean
  showError?: boolean
  showSuccess?: boolean
}

export function useApi<T>(apiFn: (...args: any[]) => Promise<any>, options: UseApiOptions = {}) {
  const { showLoading = true, showError = true, showSuccess = false } = options

  const loading: Ref<boolean> = ref(false)
  const data: Ref<T | null> = ref(null)
  const error: Ref<any> = ref(null)

  const execute = async (...args: any[]): Promise<T | null> => {
    loading.value = true
    error.value = null

    try {
      const response = await apiFn(...args)
      data.value = response.data

      if (showSuccess && response.msg) {
        ElMessage.success(response.msg)
      }

      return response.data
    } catch (err: any) {
      error.value = err

      if (showError) {
        const errorMsg = err.response?.data?.msg || err.message || '请求失败'
        ElMessage.error(errorMsg)
      }

      return null
    } finally {
      loading.value = false
    }
  }

  return {
    loading,
    data,
    error,
    execute,
  }
}
