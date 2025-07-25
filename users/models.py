from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_celery_beat.models import PeriodicTask

from config import settings
from habits.models import Habit


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


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
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="Телеграм chat_id",
        blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class UserHabitSchedule(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.email} - {self.habit.activity}"
