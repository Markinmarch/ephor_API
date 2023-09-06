from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram_bot.settings.config import CHANNEL_URL, BOT_URL


agree_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = '📝 Продолжить',
                callback_data = 'user_agree'
            )
        ]
    ]
)

continue_filling_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = '📝 Продолжить',
                callback_data = 'user_informed'
            )
        ]
    ]
)

publish_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Опубликовать',
                callback_data = 'publish'
            )
        ]
    ]
)

start_registration_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Регистрация',
                callback_data = 'create_account'
            )
        ]
    ]
)

under_post_buttons = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Отозваться',
                callback_data = 'respond_to_ad'
            )
        ],
        [
            InlineKeyboardButton(
                text = 'Бот',
                url = BOT_URL,
                callback_data = 'join_bot'
            )
        ]
    ]
)

delete_acc_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Удалить',
                callback_data = 'delete_account'
            )
        ]
    ]
)

delete_post_button = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Удалить',
                callback_data = 'delete_post'
            )
        ]
    ]
)