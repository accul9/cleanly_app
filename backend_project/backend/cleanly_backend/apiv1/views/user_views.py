from rest_framework import viewsets
from .models.models import CustomUser
from ..serializers import UserSerializer

# ユーザー登録用のViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer