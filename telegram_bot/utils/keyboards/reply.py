from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


get_phone_user = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Да! Отправить телефон',
                request_contact = True
            )
        ],
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    selective = True    
)