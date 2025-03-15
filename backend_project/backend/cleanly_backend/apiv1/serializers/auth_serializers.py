from rest_framework import serializers
from django.core.validators import RegexValidator

from ..models.t_user import CustomUser

# login
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        max_length=60,
        min_length=5,
        #validators=[RegexValidator(r"^[0-9]{8}$")],
    )
    class Meta:
        model = CustomUser
        fields = ["email", "password"]