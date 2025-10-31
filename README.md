# django-vue
python3.14+django5.2+vue3+mysql8.0


## Django部分

### 关键特性

1. **完整的认证系统**：JWT Token 认证，支持 Token 过期验证
2. **用户管理**：注册、登录、用户列表、用户详情、用户更新
3. **分页功能**：支持动态分页参数，可配置页面大小
4. **权限控制**：基于角色的访问控制
5. **统一响应格式**：所有接口返回一致的 JSON 格式
6. **错误处理**：全局异常处理和统一错误响应
7. **日志记录**：请求日志记录中间件
8. **安全性**：密码 MD5 加密，Token 认证

这个完整的项目结构可以直接运行，包含了所有必要的功能和组件。

### 运行步骤

1. **创建虚拟环境并安装依赖**

   ```bash
   conda create -n django-vue python=3.14
   conda activate django-vue
   pip install -r requirements.txt
   ```

2. **创建数据库表**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **创建超级用户（可选）**

   ```bash
   python manage.py createsuperuser
   ```

4. **运行开发服务器**

   ```bash
   python manage.py runserver
   ```

### API 使用示例

#### 注册用户

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "123456",
    "password_confirm": "123456"
  }'
```

#### 用户登录

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "123456"
  }'
```

#### 获取用户列表（需要认证）

```bash
curl -X GET "http://127.0.0.1:8000/api/users/?page=1&page_size=5" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

#### 获取用户详情（需要认证）

```bash
curl -X GET http://127.0.0.1:8000/api/users/USER_UUID/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

# Vue 3 + TypeScript 项目完整搭建指南

基于官方脚手架搭建包含完整登录注册功能的 Vue 3 项目，使用 TypeScript、Vue Router、Axios、Pinia、Element Plus 和 SCSS。

## 🚀 项目搭建步骤

### 步骤 1：使用官方脚手架创建项目

```bash
# 使用 Vue 官方脚手架创建项目
npm create vue@latest frontend

# 进入项目目录
cd vue3-ts-app

# 安装依赖
npm install
```

在创建过程中选择以下特性：

- ✅ TypeScript
- ✅ JSX Support
- ✅ Vue Router for Single Page Application
- ✅ Pinia for state management
- ✅ ESLint for code quality
- ✅ Prettier for code formatting

### 步骤 2：安装额外依赖

```bash
# 安装 UI 库和 HTTP 客户端
npm install element-plus @element-plus/icons-vue axios sass

# 安装类型定义（如需要）
npm install -D @types/node
```

### 步骤 3：启动开发服务器

```bash
npm run dev
```

## 📁 完整的项目目录结构

```
vue3-ts-app/
├── public/
│   └── favicon.ico
├── src/
│   ├── assets/
│   │   ├── base.css
│   │   └── logo.svg
│   ├── components/
│   │   ├── common/
│   │   │   ├── AppLayout.vue
│   │   │   └── LoadingSpinner.vue
│   │   └── ui/
│   │       └── BaseButton.vue
│   ├── composables/
│   │   └── useApi.ts
│   ├── router/
│   │   └── index.ts
│   ├── stores/
│   │   └── auth.ts
│   ├── types/
│   │   ├── api.ts
│   │   └── auth.ts
│   ├── utils/
│   │   ├── request.ts
│   │   ├── auth.ts
│   │   └── validation.ts
│   ├── views/
│   │   ├── auth/
│   │   │   ├── LoginView.vue
│   │   │   └── RegisterView.vue
│   │   └── HomeView.vue
│   ├── App.vue
│   ├── main.ts
│   └── style.scss
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.app.json
├── tsconfig.node.json
├── vite.config.ts
└── env.d.ts
```

## 🎯 完整的运行步骤

### 第一步：创建项目

```bash
npm create vue@latest vue3-ts-app
# 选择 TypeScript, Vue Router, Pinia, ESLint, Prettier
cd vue3-ts-app
```

### 第二步：安装依赖

```bash
npm install
npm install element-plus @element-plus/icons-vue axios sass
npm install -D @types/node
```

### 第三步：替换文件内容

将上面提供的所有文件内容复制到对应位置，覆盖或创建相应文件。

### 第四步：类型检查

```bash
npm run type-check
```

### 第五步：代码格式化

```bash
npm run lint
```

### 第六步：启动项目

```bash
npm run dev
```

### 第七步：访问应用

打开浏览器访问 `http://localhost:3000`

## ✅ 功能特性

- ✅ **Vue 3** - 最新版本的 Vue 框架
- ✅ **TypeScript** - 完整的类型安全
- ✅ **Vue Router** - 单页面应用路由
- ✅ **Pinia** - 现代化状态管理
- ✅ **Element Plus** - 企业级 UI 组件库
- ✅ **Axios** - HTTP 请求库
- ✅ **SCSS** - CSS 预处理器
- ✅ **响应式设计** - 移动端友好
- ✅ **完整的登录/注册** - 用户认证流程
- ✅ **路由守卫** - 页面访问权限控制
- ✅ **错误处理** - 统一的错误处理机制
- ✅ **加载状态** - 友好的用户反馈
- ✅ **代码规范** - ESLint + Prettier

## 🔧 配置说明

### 后端 API 配置

在 `src/utils/request.ts` 中配置后端 API 地址：

```typescript
const service: AxiosInstance = axios.create({
  baseURL: '/api', // 确保与 Django 后端 API 路径匹配
  timeout: 10000
})
```

### 代理配置

在 `vite.config.ts` 中配置代理，解决跨域问题：

```typescript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000', // Django 后端地址
      changeOrigin: true
    }
  }
}
```

## 🐛 常见问题解决

1. **TypeScript 编译错误**：运行 `npm run type-check` 查看具体错误
2. **依赖安装失败**：删除 `node_modules` 和 `package-lock.json`，重新运行 `npm install`
3. **样式不生效**：检查 `style.scss` 是否正确导入，SCSS 配置是否正确
4. **路由问题**：检查路由配置和组件导入路径
5. **API 连接失败**：确认后端服务运行且代理配置正确

这个完整的 Vue 3 + TypeScript 项目提供了现代化的前端开发体验，与你的 Django 后端完美集成，具备完整的类型安全和优秀的开发体验。
