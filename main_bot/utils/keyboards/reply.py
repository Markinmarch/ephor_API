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

route_number = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = '1'
            ),
            KeyboardButton(
                text = '2'
            ),
            KeyboardButton(
                text = '3'
            ),
            KeyboardButton(
                text = '4'
            ),
            KeyboardButton(
                text = '5'
            ),
            KeyboardButton(
                text = '6'
            ),
            KeyboardButton(
                text = '7'
            )
        ],
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    selective = True    
)