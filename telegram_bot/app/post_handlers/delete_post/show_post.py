from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToDeleteNotFound


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import CHANNEL_URL
from telegram_bot.sql_db.posts_db import posts
from telegram_bot.utils.text_content import FILTERS_MESSAGE
from telegram_bot.utils.keyboards.inline_keyboard import delete_post_button
from telegram_bot.utils.state import DeletePost


@dp.message_handler(state = DeletePost.num_post)
async def show_post(message: types.Message, state: FSMContext) -> None:
    '''
    Метод отображает список номеров id записей пользователя.
    ----------------------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объекта представления.
    '''
    request_posts_list = posts.select_posts(message.from_user.id)
    ready_posts_list = [num_posts[0] for num_posts in request_posts_list]
    if int(message.text) in ready_posts_list:
        async with state.proxy() as num_post:
            num_post['num_post'] = message.text
        get_num_post = await state.get_data()
        num_post = get_num_post['num_post']
        await message.answer(
            text = f'<a href = "{CHANNEL_URL}/{num_post}">{num_post}</a>',
            parse_mode = 'HTML',
            reply_markup = delete_post_button
        )
    else:
        await message.answer(text = FILTERS_MESSAGE['none_this_post'])
        await state.finish()            
