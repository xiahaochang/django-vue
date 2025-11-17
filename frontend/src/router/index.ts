import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import BabyTreeView from '@/views/BabyTreeView.vue'

const routes: Array<RouteRecordRaw> = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: () => import('@/views/HomeView.vue'),
  //   meta: {
  //     requiresAuth: true,
  //     title: '首页',
  //   },
  // },
  {
    path: '/',
    redirect: '/babytree',
  },
  {
    path: '/babytree',
    name: 'BabyTree',
    component: BabyTreeView,
    meta: {
      requiresAuth: true,
      title: '宝贝成长树',
    },
  },
  {
    path: '/familylove',
    name: 'FamilyLove',
    // component: () => import('@/views/FamilyLoveView.vue'),
    component: () => import('@/views/HomeView.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/auth/LoginView.vue'),
    meta: {
      requiresGuest: true,
      title: '登录',
    },
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/auth/RegisterView.vue'),
    meta: {
      requiresGuest: true,
      title: '注册',
    },
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// 路由守卫
// router.beforeEach((to, from, next) => {
//   const authStore = useAuthStore()

//   // 设置页面标题
//   if (to.meta.title) {
//     document.title = `${to.meta.title} - Little Peach`
//   }

//   if (to.meta.requiresAuth && !authStore.isLoggedIn) {
//     // 需要登录但未登录，跳转到登录页
//     next('/login')
//   } else if (to.meta.requiresGuest && authStore.isLoggedIn) {
//     // 需要游客状态但已登录，跳转到首页
//     next('/')
//   } else {
//     next()
//   }
// })

export default router
