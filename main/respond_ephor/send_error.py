import requests
from typing import Callable


from main.core.config import BOT_TOKEN, CHANNEL_ID


def send_message(message: str) -> Callable:
    response = requests.post(
        url = 'https://api.telegram.org/bot{0}/sendMessage'.format(BOT_TOKEN),
        data = {
            'chat_id': CHANNEL_ID,
            'text': message
        }
    )
    return response.json()