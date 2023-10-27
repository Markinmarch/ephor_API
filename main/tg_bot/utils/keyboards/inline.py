from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main.core.config import BOT_URL


authorization_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Отправить',
                callback_data = 'authorization'
            )
        ]
    ]
)

take_task = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Взять в работу',
                callback_data = 'take_task'
            )
        ]
    ]
)

ready_task = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Готово',
                callback_data = 'ready_task'
            )
        ]
    ]
)

send_task = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Отправить',
                callback_data = 'send_task'
            )
        ]
    ]
)