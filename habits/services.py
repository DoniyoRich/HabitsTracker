import json

from django_celery_beat.models import IntervalSchedule, PeriodicTask

from users.models import UserHabitSchedule


def create_habit_schedule(user, habit, interval_minutes=1440):
    """
    Создает периодическую задачу с интервальным расписанием раз в сутки (24 часа=1440 минут)
    """
    # Создаем интервал для повтора
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=interval_minutes,
        period=IntervalSchedule.MINUTES,
    )

    # Создаем задачу для повторения
    task = PeriodicTask.objects.create(
        interval=schedule,
        name=f'Напоминание о привычке "{habit.id}" для пользователя {user.email}',
        task='habits.tasks.send_notification_to_telegram',
        args=json.dumps([user.tg_chat_id]),
        kwargs=json.dumps({
            'message': f'Время выполнить: {habit.activity}'
        }),
        start_time=habit.time,
        enabled=True
    )

    # Сохраняем связь с пользователем
    UserHabitSchedule.objects.create(user=user, habit=habit, task=task)

    return task
