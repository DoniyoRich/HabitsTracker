import requests
from celery import shared_task
from celery.beat import logger

from config import settings


@shared_task
def send_notification_to_telegram(chat_id, message=None):
    """
    Отложенная задачи отправки уведомления в Телеграм.
    """

    if not message:
        message = "Напоминание о привычке!"

    params = {
        "text": message,
        "chat_id": chat_id
    }
    try:
        response = requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage", params=params)
        response.raise_for_status()
        return True

    except requests.RequestException as e:
        logger.error(f"Ошибка отправки сообщения в Telegram: {e}")
    return False
