from django.db import models
from django.utils import timezone
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True, help_text="用户名必须是唯一的，最长50个字符")
    password = models.CharField(max_length=32, help_text="存储MD5加密后的密码")  # MD5哈希长度
    email = models.EmailField(max_length=100, unique=True, help_text="必须是有效的邮箱地址且唯一")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
        verbose_name = '用户'
        verbose_name_plural = '用户管理'
    
    def __str__(self):
        return f"{self.username} ({self.email})"