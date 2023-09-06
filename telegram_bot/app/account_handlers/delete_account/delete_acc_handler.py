from aiogram import types
import logging


from telegram_bot.settings.setting import dp
from telegram_bot.utils.keyboards.inline_keyboard import delete_acc_button
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
        text = 'Вы уверены, что хотите удалить пользователя?',
        parse_mode = 'HTML',
        reply_markup = delete_acc_button
    )

@dp.callback_query_handler(text = 'delete_account')
async def erase_user_data(callback: types.CallbackQuery):
    if users.checking_users(callback.from_user.id) == True:
        users.delete_users(user_id = callback.from_user.id)
        await callback.answer(
            text = DELETE_ACCOUNT_MESSAGE,
            show_alert = True
        )
        logging.info(f'User {callback.from_user.id} has been deleted')
    else:
        await callback.answer(
            text = DELETE_ACCOUNT_MESSAGE,
            show_alert = True
        )
