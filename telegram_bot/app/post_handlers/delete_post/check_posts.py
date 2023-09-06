import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.sql_db.posts_db import posts
from telegram_bot.settings.config import TIMEOUT_MESSAGES
from telegram_bot.utils.text_content import CHECK_POSTS, NONE_POSTS, INTERRUPTION_MESSAGE
from telegram_bot.utils.state import DeletePost


@dp.message_handler(commands = ['my_posts'])
async def check_posts(message: types.Message, state: FSMContext) -> None:
    '''
    Метод вызывает по команде пользователя список его записей,
    оставленных им на канале.
    ----------------------------------------------------------
    parametrs:
        :commands: команда, по которой декоратор вызывается
        :message: тип представления данных
    '''
    request_posts_list = posts.select_posts(message.from_user.id)
    ready_posts_list = [num_posts[0] for num_posts in request_posts_list]
    if len(ready_posts_list) == 0:
        await message.answer(
            text = NONE_POSTS
        )
    else:
        buttons = []
        for num_post in ready_posts_list:
            buttons.append(
                types.KeyboardButton(
                    text = num_post,
                )                
            )
        buttons.append(
            types.KeyboardButton(
                text = 'Отменить ❌'
            )
        )
        keyboard = types.ReplyKeyboardMarkup(row_width = 3, resize_keyboard = True)
        await DeletePost.num_post.set()
        await message.answer(
            text = CHECK_POSTS,
            reply_markup = keyboard.add(*buttons)
        )
        # конструкция для определения времени ожидания ответа от пользователя
        # благодаря осуществляемому способу защищаем сервер от перегрузок
        await asyncio.sleep(TIMEOUT_MESSAGES['delete_post'])
        try:
            current_state = await state.get_state()
            if current_state == 'DeletePost:num_post':
                raise KeyError
        except KeyError:
            await message.answer(
                text = INTERRUPTION_MESSAGE,
                reply_markup = types.ReplyKeyboardRemove()
                )
            await state.finish()
