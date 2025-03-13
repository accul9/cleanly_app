import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

# DB操作を提供するインターフェース
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("メールアドレスは必須です")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if not password:
            raise ValueError("パスワードは必須です")
        user.set_password(password)  # パスワードをハッシュ化
        user.save(using=self._db)
        return user

    # スーパーユーザー用作成
    def create_superuser(self, email, password, **extra_fields):
        # extra_fields.setdefault("is_staff", True)
        # extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# カスタムユーザー
class CustomUser(AbstractBaseUser):
    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = 'ユーザー'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='氏名', max_length=20)
    email = models.EmailField(verbose_name='メールアドレス', max_length=60, unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=128)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # ユーザー認証に使用するフィールド
    REQUIRED_FIELDS = ['name']  # 必須のフィールド（管理者用）

    def __str__(self):
        return self.name
