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

## vue部分

