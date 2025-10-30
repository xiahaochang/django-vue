from django.db import models
from django.utils import timezone
 
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True, help_text="用户名必须是唯一的，最长50个字符")
    password = models.CharField(max_length=50, help_text="存储MD5加密后的密码")
    email = models.CharField(max_length=100,unique=True, help_text="必须是有效的邮箱地址且唯一")
    # 添加默认值
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")