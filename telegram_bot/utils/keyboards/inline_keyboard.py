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

add_name = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text = 'Ввести имя и фамилию',
                callback_data = 'add_name'
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
                text = 'Верификация',
                callback_data = 'give_phone'
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