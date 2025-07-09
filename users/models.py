from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Модель кастомного пользователя.
    """

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="e-mail"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=30,
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
