import requests

from config import settings


def send_message_to_telegram(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id
    }

    response = requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage", params=params)
