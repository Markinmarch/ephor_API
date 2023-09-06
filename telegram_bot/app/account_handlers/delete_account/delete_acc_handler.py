from aiogram import types
import logging


from telegram_bot.settings.config import CHANNEL_ID
from telegram_bot.settings.setting import dp
from telegram_bot.utils.keyboards.inline_keyboard import delete_acc_button
from telegram_bot.utils.commands import set_commands_for_new_user
from telegram_bot.sql_db.posts_db import posts
from telegram_bot.sql_db.users_db import users
from telegram_bot.utils.content.text_content import DELETE_ACCOUNT_MESSAGE, BEFORE_DEL_ACC_MESSAGE


@dp.message_handler(commands = ['delete_account'])
async def delete_account(message: types.Message) -> None:
    '''
    Данный метод отправляет пользователю предупреждение
    о удалении аккаунта и кнопку подтверждения удаления
    аккаунта.
    ---------------------------------------------------
        parametrs:
            :commands: команда вызова обработчика
            :message: тип объекта представления
    '''
    await message.answer(
        text = BEFORE_DEL_ACC_MESSAGE,
        parse_mode = 'HTML',
        reply_markup = delete_acc_button
    )

@dp.callback_query_handler(text = 'delete_account')
async def erase_user_data(callback: types.CallbackQuery):
    if users.checking_users(callback.from_user.id) == True:
        users.delete_users(user_id = callback.from_user.id)
        await set_commands_for_new_user(bot = callback.bot)
        await callback.answer(
            text = DELETE_ACCOUNT_MESSAGE,
            show_alert = True
        )
        user_posts = posts.select_posts(callback.from_user.id)
        user_posts_list = [num_posts[0] for num_posts in user_posts]
        for num_post in user_posts_list:
            await callback.bot.delete_message(
                chat_id = CHANNEL_ID,
                message_id = num_post
            )
            posts.delete_post(num_post)
        logging.info(f'User {callback.from_user.id} has been deleted')
    else:
        await callback.answer(
            text = DELETE_ACCOUNT_MESSAGE,
            show_alert = True
        )
