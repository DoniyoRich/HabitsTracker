from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from config import settings


class Award(models.Model):
    """
    Класс вознаграждений.
    """

    award = models.CharField(max_length=100, verbose_name="Вознаграждение")

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"

    def __str__(self):
        return self.award


class Habit(models.Model):
    """
    Класс привычек.
    Может быть как полезной привычкой, так и связанной.
    В модели проводится валидация на одновременное заполнение полей вознаграждения и связанной привычки.
    Можно заполнить только одно из двух полей. В противном случае вызывается исключение.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                             verbose_name="Пользователь", null=True, blank=True)
    activity = models.CharField(max_length=100, verbose_name="Действие")
    time = models.TimeField(verbose_name="Время начала действия привычки")
    location = models.CharField(max_length=100, verbose_name="Место выполнения привычки")
    is_pleasant = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    linked = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Связанная привычка",
                               null=True, blank=True, related_name="habits_linked")
    award = models.ForeignKey(Award, on_delete=models.SET_NULL, null=True, blank=True, related_name="awards")
    frequency = models.PositiveIntegerField(verbose_name="Периодичность",
                                            validators=[MinValueValidator(1), MaxValueValidator(7)])
    implementation_time = models.PositiveIntegerField(verbose_name="Время выполнения в секундах", default=120)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ['time']

    def __str__(self):
        return f"Я буду {self.activity} в {self.time} в {self.location})"
