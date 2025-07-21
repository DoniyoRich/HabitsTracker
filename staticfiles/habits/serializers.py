from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from habits.models import Award, Habit


class HabitSerializer(ModelSerializer):
    """
    Сериализатор для модели полезной привычки.
    """

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        errors = {}

        is_pleasant = data.get('is_pleasant', False)
        award = data.get('award')
        linked = data.get('linked')
        implementation_time = data.get('implementation_time')
        frequency = data.get('frequency')

        # проверка для приятных привычек
        if is_pleasant:
            if award:
                errors['award'] = "Приятная привычка не может иметь вознаграждения"
            if linked:
                errors['linked'] = "Приятная привычка не может быть связанной"
        else:
            # для полезных привычек должно быть указано либо вознаграждение, либо связанная привычка
            if not award and not linked:
                errors['non_field_errors'] = ["Для полезной привычки укажите вознаграждение или связанную привычку"]

        # проверка для связанных привычек
        if linked:
            if not linked.is_pleasant:
                errors['linked'] = "Связанная привычка должна быть приятной"
            if award:
                errors['non_field_errors'] = ["Можно указать только вознаграждение ИЛИ связанную привычку, но не оба"]

        # проверка времени выполнения
        if implementation_time is not None:
            if implementation_time < 1 or implementation_time > 120:
                errors['implementation_time'] = "Время выполнения должно быть от 1 до 120 секунд"

        # проверка периодичности (не реже 1 раза в неделю)
        if frequency is not None and frequency > 7:
            errors['frequency'] = "Периодичность не может быть реже 1 раза в 7 дней"

        if errors:
            raise serializers.ValidationError(errors)

        return data


class AwardSerializer(ModelSerializer):
    """
    Сериализатор для модели вознаграждения.
    """

    class Meta:
        model = Award
        fields = "__all__"
