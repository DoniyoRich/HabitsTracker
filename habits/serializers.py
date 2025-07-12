from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from habits.models import Habit, HabitLinked, Award


class HabitSerializer(ModelSerializer):
    """
    Сериализатор для модели полезной привычки.
    """

    class Meta:
        model = Habit
        fields = "__all__"


class HabitLinkedSerializer(ModelSerializer):
    """
    Сериализатор для модели связанной привычки.
    """

    class Meta:
        model = HabitLinked
        fields = "__all__"


class AwardSerializer(ModelSerializer):
    """
    Сериализатор для модели вознаграждения.
    """

    class Meta:
        model = Award
        fields = "__all__"
