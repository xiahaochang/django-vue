from rest_framework import serializers
from ..models import User

class UserListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'created_at']
        read_only_fields = fields

class UserDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'password']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active']
        extra_kwargs = {
            'username': {'min_length': 3}
        }
    
    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("用户名只能包含字母和数字")
        return value