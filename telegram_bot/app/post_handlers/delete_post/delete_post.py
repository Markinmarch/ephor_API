from aiogram import types
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import CHANNEL_ID
from telegram_bot.sql_db.posts_db import posts
from telegram_bot.utils.state import DeletePost
from telegram_bot.utils.content.text_content import DELETE_POST_MESSAGE


@dp.callback_query_handler(text = 'delete_post', state = DeletePost.num_post)
async def delete_post(callback: types.CallbackQuery, state: FSMContext) -> None:
    '''
    Метод отображает ссылку с виджетом выбраной записи по её
    номеру и удаляет её.
    ----------------------------------------------------------
    parametrs:
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :callback: тип объекта представления.
        :text: вызов callback_query по ключевому слову.
    '''
    get_num_post = await state.get_data()
    num_post = get_num_post['num_post']
    await callback.bot.delete_message(
        chat_id = CHANNEL_ID,
        message_id = num_post,
    )
    posts.delete_post(num_post)
    await callback.message.answer(
        text = DELETE_POST_MESSAGE,
        reply_markup = types.ReplyKeyboardRemove()
    )
    await state.finish()