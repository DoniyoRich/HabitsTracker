from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
    """
    Сериализатор для модели пользователя.
    """

    class Meta:
        model = CustomUser
        # fields = ("id", "email", "avatar", "phone_number", "city")
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserSerializerLimited(ModelSerializer):
    """
    Сериализатор для модели пользователя, поля только id, email, avatar, city, phone.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "email", "avatar", "phone_number", "city")
