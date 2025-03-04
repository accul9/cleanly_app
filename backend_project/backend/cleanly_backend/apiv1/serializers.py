from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    is_completed_label = serializers.SerializerMethodField()
    frequency_label = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {
            "is_completed": {"required": False},
            "default": False,
            "title": {"error_messages": {"required": "タイトルは必須です。"}},
        }

        def is_completed_label(self, obj):
            return "完了" if obj.is_completed else "未着手"

        def frequency_label(self, obj):
            return obj.get_frequency_display()
