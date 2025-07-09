from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import UserSerializer, UserSerializerLimited


class UserRegisterView(CreateAPIView):
    """
    API регистрации пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     user = serializer.save(is_active=True)
    #     user.set_password(user.password)
    #     user.save()


class UserListAPIView(ListAPIView):
    """
    API получения списка пользователей.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    # permission_classes = [IsModerator]


class UserDetailAPIView(RetrieveAPIView):
    """
    API получения одного пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    # permission_classes = [IsModerator | IsOwner]


class UserUpdateAPIView(UpdateAPIView):
    """
    API редактирования профиля пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    # permission_classes = [IsOwner]


class UserDeleteAPIView(DestroyAPIView):
    """
    API удаления профиля пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    # permission_classes = [IsModerator]
