"""
Текстовые сообщения вынесены в отдельный файл
для быстрого и более эффективного форматирования
"""

POST_CONTENT = (
    '<b><u>{0}</u></b>\n'
    '<b>→ Содержание:</b> {1}\n'
    '<b>→ Условия:</b> <i>{2}</i>'
)

FEEDBACK = 'Пользователь <a href="{0}">{1}</a> отозвался на Ваше <a href="{2}/{3}">объявление</a>.'

GIVE_PHONE = 'Согласны дать нам свой номер телефона?'

VERIFICATION = 'Верификация прошла успешно'

CREATE_POST_MESSAGE = {
    'direction': 'Пожалуйста, определите тему для Вашей записи',
    'title': 'Напишите краткое описание записи (напр. Подработка/Услуги сантехника/Дрова/Уголь/Вывезти мусор)',
    'text': 'Напишите содержание записи с подробностями',
    'conditions': 'Опишите условия работы - зарплату/цену за заказ',
    'photo': 'Можете прикрепить одну фотографию к записи по желанию либо опубликовать свою запись сразу'
}

PUBLICATION_ACCOUNCEMENT = 'Ваше объявление в ближайшее время будет опубликовано на канале'

GIVE_NAME = 'Для верификации введите подлинное имя и фамилию/отчество'

OUTSIDER_MESSAGE = 'К сожалению, мы не можем предоставить Вам право пользоваться телеграм-каналом'

BEFORE_DEL_ACC_MESSAGE = 'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены. У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.'

DELETE_ACCOUNT_MESSAGE = 'Ваш аккаунт удалён'

WAITING_MESSAGE = 'Вы слишком часто используете эту команду. Подождите 5 минут'

WARNING_MESSAGE_BEFORE_DELETION_ACC = (
    'Если Вы удалите свой аккаунт, то и все Ваши записи с канала будут удалены.\n'
    'У Вас больше не будет возможности создавать посты, но Вы по прежнему сможете отзываться на них.'
)

FEEDBACK_SEND = 'Отзыв отправлен'

ALREADY_RESPONDED_MESSAGE = 'Вы уже отзывались на эту запись. Если запись ещё актуальна, то её автор Вам напишет'

LIMIT_WARNING_PUBLICATION_MESSAGE = 'Ваш лимит подаваемых записей на сегодня закончился.'

INTERRUPTION_MESSAGE = 'Процесс прерван из-за долгого ожидания ответа.'

CHECK_POSTS = 'Выберите номер записи из предложенного списка:'

NONE_POSTS = 'У Вас не имеется записей на канале.'

DELETE_POST_MESSAGE = 'Ваша запись удалёна.'

FILTERS_MESSAGE = {
    'command_brake': 'Команда отменена.',
    'none_this_post': 'У Вас не имеется записи под данным номером.',
    'bad_words': 'Пожалуйста, не используйте ненормативную лексику.\n'
                 'Помните о <b><a href = "https://telegra.ph/Pravila-polzovaniya-telegram-botom-02-25">правилах</a></b> пользования каналом!',
    'create_post': {
        'repeat_title': 'Пожалуйста, опишите деятельность короче. Необходимо написать не ,более двадцати символов.',
        'repeat_text': 'Пожалуйста, опишите деятельность подробнее. Необходимо написать не менее двадцати символов.',
        'repeat_direction': 'Пожалуйста, выберите направление из предложенных: Услуга, Предложение или Биржа'
    },
    'registration_user': {
        'add_name': 'Пожалуйста, введите своё имя. Можно использовать псевдоним для дополнителной безопасности.',
        'add_age': 'Укажите свой действительный возраст.',
        'add_gender': 'Укажите свой пол.',
        'add_phone': 'Согласны дать нам свой номер телефона?'
    },
}