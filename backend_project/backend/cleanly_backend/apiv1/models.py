from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Task(models.Model):
    class Meta:
        db_table = "task"
        verbose_name = verbose_name_plural = (
            "タスク"  # verbose_name_pluralを使って複数形のラベルを指定
        )

    FREQUENCY_CHOICES = [
        ("D", "日"),  # Daily
        ("W", "週"),  # Weekly
        ("M", "月"),  # Monthly
    ]

    REPEAT_OPTIONS = [
        ("none", "なし"),
        ("daily", "毎日"),
        ("weekly", "毎週"),
        ("monthly", "毎月"),
    ]

    # verbose_nameを使ってフィールドのラベルを日本語で指定
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー")
    title = models.CharField(verbose_name="タイトル", max_length=20)
    memo = models.TextField(verbose_name="メモ", null=True, blank=True)
    is_completed = models.BooleanField(verbose_name="完了", default=False)
    due_date = models.DateField(verbose_name="期限", null=True, blank=True)
    frequency = models.CharField(
        verbose_name="頻度", max_length=1, choices=FREQUENCY_CHOICES, default="D"
    )
    repeat = models.CharField(max_length=10, choices=REPEAT_OPTIONS, default="none")
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    # 繰り返しのルール
    def update_due_date(self):
        if self.recurrence_rule == "daily":
            self.due_date += datetime.timedelta(days=1)
        elif self.recurrence_rule == "weekly":
            self.due_date += datetime.timedelta(weeks=1)
        elif self.recurrence_rule == "monthly":
            self.due_date = self.due_date.replace(
                month=self.due_date.month + 1 if self.due_date.month < 12 else 1,
                year=(
                    self.due_date.year
                    if self.due_date.month < 12
                    else self.due_date.year + 1
                ),
            )

    def __str__(self):
        frequency_labels = {"D": "日", "W": "週", "M": "月"}
        frequency_display = frequency_labels.get(
            self.frequency, "日"
        )  # Default to "日" (Daily)

        # メモの有無によって表示を変える
        memo_display = f" | メモ: {self.memo}" if self.memo else ""

        # Handle cases where due_date is None (fallback to "未設定")
        due_date_display = (
            self.due_date.strftime("%Y-%m-%d") if self.due_date else "未設定"
        )
        repeat_display = dict(self.REPEAT_OPTIONS).get(self.repeat, "なし")
        return f"{self.title} - 期限: {due_date_display} | 頻度: {frequency_display}| 繰り返し: {repeat_display}{memo_display}"


# class TaskTemplate(models.Model):
# class CompletedTask(models.Model):
# class TaskUser(models.Model):
