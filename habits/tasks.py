from celery import shared_task

import requests

from config import settings


@shared_task
def send_notification_to_telegram(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id
    }

    response = requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage", params=params)
