from rest_framework import serializers
# from .views.models.models import Task
from ..models.models import Task 

class TaskSerializer(serializers.ModelSerializer):
    is_completed_label = serializers.SerializerMethodField()
    frequency_label = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {
            "is_completed": {"required": False, "default": False},
            "title": {"error_messages": {"required": "タイトルは必須です。"}},
        }

    # メソッド名はget_フィールド名の形式で定義
    def get_is_completed_label(self, obj):
        return "完了" if obj.is_completed else "未着手"

    def get_frequency_label(self, obj):
        return obj.get_frequency_display()
