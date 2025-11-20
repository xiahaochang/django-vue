<template>
  <div class="app-layout">
    <el-container class="layout-container">
      <!-- 桃子风格顶部导航栏 -->
      <el-header class="peach-header">
        <div class="header-background">
          <div class="peach-shape shape-1"></div>
          <div class="peach-shape shape-2"></div>
          <div class="peach-shape shape-3"></div>
          <div class="peach-gradient"></div>
        </div>

        <div class="header-content">
          <!-- 左侧品牌区域 -->
          <div class="brand-section">
            <div class="logo">
              <div class="logo-icon">
                <div class="logo-peach">
                  <div class="peach-fruit"></div>
                  <div class="peach-leaf"></div>
                </div>
              </div>
              <h1 class="brand-name">小桃子</h1>
            </div>
          </div>

          <!-- 中央导航菜单 -->
          <div class="nav-section">
            <nav class="peach-nav">
              <router-link
                v-for="item in navItems"
                :key="item.id"
                :to="item.path"
                class="nav-item"
                :class="{ active: activeNav === item.id }"
                @click="setActiveNav(item)"
              >
                <span class="nav-icon">{{ item.icon }}</span>
                <span class="nav-text">{{ item.text }}</span>
                <span class="nav-underline"></span>
              </router-link>
            </nav>
          </div>

          <!-- 右侧用户区域 -->
          <div class="user-section">
            <div class="action-buttons">
              <button class="action-btn search-btn">
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M21 21L16.514 16.506L21 21ZM19 10.5C19 15.194 15.194 19 10.5 19C5.806 19 2 15.194 2 10.5C2 5.806 5.806 2 10.5 2C15.194 2 19 5.806 19 10.5Z"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </button>

              <button class="action-btn notification-btn">
                <svg
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M18 8C18 6.4087 17.3679 4.88258 16.2426 3.75736C15.1174 2.63214 13.5913 2 12 2C10.4087 2 8.88258 2.63214 7.75736 3.75736C6.63214 4.88258 6 6.4087 6 8C6 15 3 17 3 17H21C21 17 18 15 18 8Z"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M13.73 21C13.5542 21.3031 13.3019 21.5547 12.9982 21.7295C12.6946 21.9044 12.3504 21.9965 12 21.9965C11.6496 21.9965 11.3054 21.9044 11.0018 21.7295C10.6982 21.5547 10.4458 21.3031 10.27 21"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
                <span class="notification-dot"></span>
              </button>
            </div>

            <div class="user-profile">
              <el-dropdown
                trigger="click"
                placement="bottom-end"
                @command="handleCommand"
                class="user-dropdown"
              >
                <div class="user-trigger">
                  <div class="avatar-container">
                    <div class="user-avatar">
                      <img :src="userAvatar" alt="用户头像" />
                    </div>
                    <div class="status-indicator"></div>
                  </div>

                  <div class="user-info">
                    <div class="user-name">{{ authStore.user?.username }}</div>
                    <div class="user-role">创意总监</div>
                  </div>

                  <el-icon class="dropdown-arrow"><ArrowDown /></el-icon>
                </div>

                <template #dropdown>
                  <el-dropdown-menu class="peach-dropdown-menu">
                    <el-dropdown-item command="profile" class="menu-item">
                      <el-icon><User /></el-icon>
                      <span>个人资料</span>
                    </el-dropdown-item>
                    <el-dropdown-item command="settings" class="menu-item">
                      <el-icon><Setting /></el-icon>
                      <span>账户设置</span>
                    </el-dropdown-item>
                    <el-dropdown-item command="collection" class="menu-item">
                      <el-icon><Collection /></el-icon>
                      <span>我的收藏</span>
                    </el-dropdown-item>
                    <el-dropdown-divider />
                    <el-dropdown-item command="logout" class="menu-item logout">
                      <el-icon><SwitchButton /></el-icon>
                      <span>退出登录</span>
                    </el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </div>
          </div>
        </div>
      </el-header>

      <!-- 主内容区域 -->
      <el-main class="layout-main">
        <div class="main-content">
          <div class="content-wrapper">
            <div class="content-area">
              <slot />
            </div>
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, watch, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { ArrowDown, User, Setting, SwitchButton, Collection } from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const activeNav = ref('babytree')

// 导航项数据
const navItems = [
  { id: 'babytree', text: '宝贝成长树', path: '/babytree', icon: '🍑' },
  { id: 'familylove', text: '爸爸妈妈爱你', path: '/familylove', icon: '🧑🏻‍👩🏻‍👧🏻' },
  // { id: 'gallery', text: '作品集', path: '/gallery', icon: '🎨' },
  // { id: 'projects', text: '项目', path: '/projects', icon: '📂' },
  // { id: 'inspire', text: '灵感', path: '/inspire', icon: '✨' },
]

// 用户头像
const userAvatar = computed(() => {
  return 'https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=128&h=128&q=80'
})

// 设置当前激活的导航项
const setActiveNav = (item: any) => {
  activeNav.value = item.id
}
// 根据当前路由更新激活状态
const updateActiveNav = () => {
  const currentPath = route.path
  const currentNav = navItems.find((item) => item.path === currentPath)
  if (currentNav) {
    activeNav.value = currentNav.id
  }
}

const handleCommand = async (command: string) => {
  switch (command) {
    case 'logout':
      try {
        await ElMessageBox.confirm('确定要退出登录吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
        })
        authStore.logout()
        ElMessage.success('已退出登录')
        router.push('/login')
      } catch {
        // 用户取消操作
      }
      break
    case 'profile':
      ElMessage.info('个人资料功能开发中...')
      break
    case 'settings':
      ElMessage.info('账户设置功能开发中...')
      break
    case 'collection':
      ElMessage.info('我的收藏功能开发中...')
      break
  }
}

// 监听路由变化
watch(
  () => route.path,
  () => {
    updateActiveNav()
  },
)
// 初始化时设置激活状态
onMounted(() => {
  updateActiveNav()
})
</script>

<style lang="scss" scoped>
.app-layout {
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #fff9f5;
  font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
  overflow: hidden; /* 防止整个应用出现滚动条 */
}

.layout-container {
  height: 100%;
  display: flex;
  flex-direction: column;
}

// 桃子风格顶部导航栏
.peach-header {
  height: 80px;
  padding: 0;
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg, #ffe8e8 0%, #ffd6d6 100%);
  box-shadow: 0 4px 20px rgba(255, 150, 150, 0.1);
  z-index: 1000;
  flex-shrink: 0; /* 防止导航栏被压缩 */

  .header-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    overflow: hidden;

    .peach-shape {
      position: absolute;
      border-radius: 50%;
      opacity: 0.15;
      background: linear-gradient(135deg, #ff9e9e 0%, #ff7b7b 100%);

      &.shape-1 {
        width: 140px;
        height: 140px;
        top: -50px;
        left: 5%;
        filter: blur(10px);
      }

      &.shape-2 {
        width: 90px;
        height: 90px;
        bottom: -30px;
        right: 10%;
        filter: blur(8px);
      }

      &.shape-3 {
        width: 70px;
        height: 70px;
        top: 15px;
        right: 20%;
        filter: blur(6px);
      }
    }

    .peach-gradient {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(
        90deg,
        rgba(255, 235, 235, 0.6) 0%,
        rgba(255, 225, 225, 0.4) 50%,
        rgba(255, 235, 235, 0.6) 100%
      );
    }
  }

  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 30px;
    position: relative;
    z-index: 1;
  }
}

// 品牌区域样式
.brand-section {
  .logo {
    display: flex;
    align-items: center;

    .logo-icon {
      position: relative;
      width: 40px;
      height: 40px;
      margin-right: 12px;
      display: flex;
      align-items: center;
      justify-content: center;

      .logo-peach {
        position: relative;
        width: 32px;
        height: 32px;

        .peach-fruit {
          width: 28px;
          height: 28px;
          border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
          background: linear-gradient(135deg, #ff9e9e 0%, #ff7b7b 100%);
          position: relative;
          z-index: 2;
          box-shadow: 0 2px 4px rgba(255, 120, 120, 0.3);

          &::after {
            content: '';
            position: absolute;
            top: 6px;
            left: 8px;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            filter: blur(1px);
          }
        }

        .peach-leaf {
          position: absolute;
          top: 2px;
          right: 4px;
          width: 10px;
          height: 8px;
          border-radius: 50% 0 50% 50%;
          background: #a5d6a7;
          transform: rotate(45deg);
          z-index: 3;
          box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
      }
    }

    .brand-name {
      margin: 0;
      color: #ff6b6b;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 2px 4px rgba(255, 107, 107, 0.1);
    }
  }
}

// 导航菜单样式
.nav-section {
  flex: 1;
  display: flex;
  justify-content: center;

  .peach-nav {
    display: flex;
    align-items: center;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 8px;
    box-shadow: 0 4px 12px rgba(255, 150, 150, 0.15);
    border: 1px solid rgba(255, 200, 200, 0.3);

    .nav-item {
      display: flex;
      align-items: center;
      padding: 10px 20px;
      text-decoration: none;
      color: #ff8e8e;
      font-weight: 500;
      border-radius: 12px;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;

      &:hover {
        color: #ff6b6b;
        background: rgba(255, 107, 107, 0.08);
      }

      &.active {
        color: #ff6b6b;
        background: rgba(255, 107, 107, 0.12);

        .nav-underline {
          width: 100%;
          opacity: 1;
        }
      }

      .nav-icon {
        margin-right: 8px;
        font-size: 16px;
      }

      .nav-text {
        font-size: 15px;
      }

      .nav-underline {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #ff9e9e 0%, #ff6b6b 100%);
        border-radius: 2px;
        opacity: 0;
        transition: all 0.3s ease;
      }
    }
  }
}

// 用户区域样式
.user-section {
  display: flex;
  align-items: center;

  .action-buttons {
    display: flex;
    margin-right: 20px;

    .action-btn {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.7);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 200, 200, 0.3);
      color: #ff8e8e;
      cursor: pointer;
      transition: all 0.3s ease;
      margin-left: 8px;
      position: relative;

      &:hover {
        color: #ff6b6b;
        background: rgba(255, 107, 107, 0.1);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255, 150, 150, 0.2);
      }

      &.notification-btn {
        .notification-dot {
          position: absolute;
          top: 10px;
          right: 10px;
          width: 8px;
          height: 8px;
          border-radius: 50%;
          background: #ff6b6b;
          border: 2px solid rgba(255, 255, 255, 0.9);
        }
      }
    }
  }

  .user-profile {
    .user-dropdown {
      .user-trigger {
        display: flex;
        align-items: center;
        padding: 8px 12px;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 200, 200, 0.3);

        &:hover {
          background: rgba(255, 255, 255, 0.7);
          box-shadow: 0 4px 12px rgba(255, 150, 150, 0.15);
        }

        .avatar-container {
          position: relative;
          margin-right: 12px;

          .user-avatar {
            width: 44px;
            height: 44px;
            border-radius: 14px;
            overflow: hidden;
            border: 2px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 4px 12px rgba(255, 150, 150, 0.15);

            img {
              width: 100%;
              height: 100%;
              object-fit: cover;
            }
          }

          .status-indicator {
            position: absolute;
            bottom: 2px;
            right: 2px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #a5d6a7;
            border: 2px solid rgba(255, 255, 255, 0.9);
          }
        }

        .user-info {
          margin-right: 12px;
          text-align: left;

          .user-name {
            font-weight: 600;
            color: #ff6b6b;
            font-size: 15px;
            line-height: 1.2;
          }

          .user-role {
            font-size: 12px;
            color: #ff8e8e;
          }
        }

        .dropdown-arrow {
          color: #ff8e8e;
          transition: transform 0.3s ease;
        }
      }
    }
  }
}

// 自定义下拉菜单样式
:deep(.peach-dropdown-menu) {
  border: none;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(255, 150, 150, 0.15);
  padding: 8px;
  margin-top: 8px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 200, 200, 0.3);

  .menu-item {
    display: flex;
    align-items: center;
    padding: 10px 12px;
    border-radius: 10px;
    margin: 2px 0;
    color: #ff8e8e;
    font-size: 14px;

    .el-icon {
      margin-right: 10px;
      font-size: 16px;
      color: #ff8e8e;
    }

    &:hover {
      background: rgba(255, 107, 107, 0.1);
      color: #ff6b6b;

      .el-icon {
        color: #ff6b6b;
      }
    }

    &.logout {
      color: #ff6b6b;

      &:hover {
        background: rgba(255, 107, 107, 0.1);
      }
    }
  }

  .el-dropdown-menu__item {
    padding: 0;
  }

  .el-dropdown-menu__item:not(.is-disabled):hover {
    background-color: transparent;
    color: inherit;
  }
}

// 主内容区域样式 - 优化滚动体验
.layout-main {
  flex: 1;
  padding: 0;
  background-color: #fff9f5;
  overflow: hidden; /* 隐藏默认滚动条 */
  display: flex;
  flex-direction: column;
}

.main-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 12px;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;

  .content-wrapper {
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(255, 200, 200, 0.1);
    overflow: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(255, 225, 225, 0.5);
  }

  .content-area {
    padding: 30px;
    flex: 1;
    overflow-y: auto;
  }
}
</style>
