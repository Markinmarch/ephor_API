from aiogram import types
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import CHANNEL_ID
from telegram_bot.sql_db.posts_db import posts
from telegram_bot.utils.state import AddPost
from telegram_bot.utils.keyboards.inline_keyboard import under_post_buttons
from telegram_bot.utils.content.text_content import POST_CONTENT, PUBLICATION_ACCOUNCEMENT


@dp.message_handler(state = AddPost.photo, content_types = types.ContentType.ANY)
async def add_photo__cmd_publish(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    фотографию объявления, формирует данные,
    публикует на канале и записывает id автора поста
    с id поста в БД и завершает State()
    -----------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления
        :content_types: тип данных
    '''
    if message.text == 'Продолжить публикацию':
        await state.update_data(photo = 'standart_photo')
    else:
        await state.update_data(photo = message.photo[0].file_id)
    await message.answer(
        text = PUBLICATION_ACCOUNCEMENT,
        reply_markup = types.ReplyKeyboardRemove()
        )

    for_post_data = await state.get_data()
    caption = POST_CONTENT.format(
        for_post_data.get('title'),
        for_post_data.get('text'),
        for_post_data.get('conditions')
    )
    if for_post_data.get('photo') == 'standart_photo':
        photo = types.InputFile(path_or_bytesio = 'telegram_bot/utils/content/media_content/botik.jpg')
    else:
        photo = for_post_data.get('photo')
    msg = await message.bot.send_photo(
        chat_id = CHANNEL_ID,
        photo = photo,
        caption = caption,
        parse_mode = 'HTML',
        reply_markup = under_post_buttons
    )
    channel_msg_id = msg['message_id']
    # записываем id поста и id пользователя в БД
    posts.insert_post(
        post_id = channel_msg_id,
        user_id = message.from_user.id
    )
    await state.finish()