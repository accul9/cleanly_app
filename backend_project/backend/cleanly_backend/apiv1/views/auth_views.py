from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from ..serializers import LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ログインAPI
class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    @method_decorator(csrf_protect)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 認証
        user = authenticate(
            request=request,
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return Response(
                {"msg": "メールアドレスまたはパスワードが間違っています"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        login(request, user)
        return Response(
            {
                "id": user.id,
                "email": user.email,
                "name": user.name,
            },
            status=status.HTTP_200_OK,
        )
# ログアウト
class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {
                "msg": "ログアウトしました。",
            },
            status=status.HTTP_200_OK,
        )