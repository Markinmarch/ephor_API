from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


direction_detection_buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Предложениe'
            )
        ],
        [
            KeyboardButton(
                text = 'Услуга'
            )
        ],
        [
            KeyboardButton(
                text = 'Биржа'
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
    input_field_placeholder = 'Тема для публикации записи',
    selective = True
)

choose_gender = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Мужской'
            )
        ],
        [
            KeyboardButton(
                text = 'Женский'
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
    input_field_placeholder = 'Пол пользователя',
    selective = True
)

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

continue_publishing = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Продолжить публикацию'
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

by_agreement = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'По договорённости'
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
    selective = False,
    input_field_placeholder = 'Введите стоимость либо нажмите кнопку'
)

canseled = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(
                text = 'Отменить ❌'
            )
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    selective = False,
)