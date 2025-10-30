from rest_framework import serializers
from ..models import User
from common.utils import md5_encrypt

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=3)
    password = serializers.CharField(required=True, write_only=True, min_length=6)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("用户名或密码错误")
        
        if not user.is_active:
            raise serializers.ValidationError("用户已被禁用，请联系管理员")
        
        encrypted_password = md5_encrypt(password)
        if user.password != encrypted_password:
            raise serializers.ValidationError("用户名或密码错误")
        
        data['user'] = user
        return data

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6},
            'username': {'min_length': 3}
        }
    
    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("用户名只能包含字母和数字")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("用户名已存在")
        return value
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("邮箱已被注册")
        return value
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "两次密码输入不一致"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        validated_data['password'] = md5_encrypt(validated_data['password'])
        return super().create(validated_data)