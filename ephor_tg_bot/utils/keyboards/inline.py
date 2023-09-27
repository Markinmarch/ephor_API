from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ephor_tg_bot.core.config import BOT_URL


authorization_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Отправить ',
                callback_data = 'authorization'
            )
        ]
    ]
)
