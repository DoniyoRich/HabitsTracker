from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

from config import settings
from config.constants import TIME_UNITS


class HabitLinked(models.Model):
    """
    Класс связанных привычек, взаимоисключающий с классом вознаграждений
    """

    activity = models.CharField(max_length=100, verbose_name="Связанная привычка")

    class Meta:
        verbose_name = "Связанная привычка"
        verbose_name_plural = "Связанные привычки"

    def __str__(self):
        return self.activity


class Award(models.Model):
    """
    Класс вознаграждений, взаимоисключающий с классом связанных привычек.
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
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                             verbose_name="Пользователь", null=True, blank=True)
    activity = models.CharField(max_length=100, verbose_name="Действие")
    time = models.TimeField(verbose_name="Время начала действия")
    location = models.CharField(max_length=100, verbose_name="Место выполнения")
    award = models.ForeignKey(Award, on_delete=models.SET_NULL, null=True, blank=True, related_name="awards")
    linked = models.OneToOneField(HabitLinked, on_delete=models.SET_NULL, null=True, blank=True, related_name="habit")
    frequency = models.PositiveIntegerField(verbose_name="Периодичность",
                                            validators=[MinValueValidator(1), MaxValueValidator(1000)])
    time_unit = models.CharField(max_length=15, choices=TIME_UNITS, default="minutes", verbose_name="Единица времени")
    implementation_time = models.PositiveIntegerField(verbose_name="Время выполнения", default=2, db_index=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.activity} в {self.time} в {self.location})"

    def clean(self):
        """
        Проверка взаимного исключения award и linked.
        """

        if self.award and self.linked:
            raise ValidationError("Можно указать только вознаграждение ИЛИ связанную привычку, но не оба одновременно.")

        if self.implementation_time < 1:
            raise ValidationError("Время выполнения не может быть меньше 1.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
