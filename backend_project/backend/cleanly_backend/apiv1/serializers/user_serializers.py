from rest_framework import serializers
from django.core.validators import RegexValidator

from ..models.t_user import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'blank': '氏名は空にできません。',
                }
            },
            'email': {
                'error_messages': {
                    'blank': 'メールアドレスは空にできません。',
                }
            },
            'password': {
                'error_messages': {
                    'blank': 'パスワードは空にできません。',
                }
            }
        }
    def create(self, validated_data):
        # パスワードのハッシュ化を行う
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)  # パスワードをハッシュ化
        user.save()
        return user
