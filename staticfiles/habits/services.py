import json

from django.db import IntegrityError
from django.utils import timezone
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from users.models import UserHabitSchedule


def create_habit_schedule(owner, habit):
    """
    Создает периодическую задачу с интервальным расписанием раз в сутки (24 часа=1440 минут)
    """
    try:
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1440,
            period=IntervalSchedule.MINUTES,
            defaults={'every': 1440, 'period': IntervalSchedule.MINUTES}
        )
    except IntegrityError:
        # если возникла ошибка уникальности — берем существующий интервал
        schedule = IntervalSchedule.objects.filter(
            every=1440,
            period=IntervalSchedule.MINUTES
        ).first()

    # создаем задачу для повторения
    task = PeriodicTask.objects.create(
        interval=schedule,
        name=f'Напоминание о привычке "{habit.activity}" для пользователя {owner.email}',
        task='habits.tasks.send_notification_to_telegram',
        args=json.dumps([owner.tg_chat_id]),
        kwargs=json.dumps({
            'message': f'Время выполнить привычку: {habit.activity}'
        }),
        start_time=timezone.now().replace(
            hour=habit.time.hour,
            minute=habit.time.minute),
        enabled=True
    )

    UserHabitSchedule.objects.create(owner=owner, habit=habit, task=task)

    return task
