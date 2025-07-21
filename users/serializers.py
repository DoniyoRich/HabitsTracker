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


class UserSerializerLimited(ModelSerializer):
    """
    Сериализатор для модели пользователя, поля только id, email, avatar, city, phone.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "email", "avatar", "phone_number", "city")
