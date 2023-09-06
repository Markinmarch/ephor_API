from aiogram import types
import logging


from telegram_bot.settings.setting import dp
from telegram_bot.utils.content.text_content import WELCOME, IF_USER_HAVE_ACCOUNT, UPDATE_MESSAGE
from telegram_bot.utils.keyboards.inline_keyboard import agree_button
from telegram_bot.sql_db.users_db import users


@dp.callback_query_handler(text = 'create_account')
async def user_agreement_via_query(callback: types.CallbackQuery) -> None:
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшую регистрацию через запрос (нажатие кнопки)
    ----------------------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :callback: тип объекта представления
    '''
    await callback.message.answer(
        text = WELCOME,
        parse_mode = 'HTML',
        reply_markup = agree_button
    )

@dp.message_handler(commands = ['create_account'])
async def user_agreement_via_command(message: types.Message) -> None:
    '''
    Данный объект реализует получение согласия от пользователя
    на дальнейшую регистрацию через команду
    ----------------------------------------------------------
    parametrs:
        :commands: команда вызова обработчика
        :message: тип объекта представления
    '''
    if users.checking_users(message.from_user.id) == False:
        await message.answer(
            text = WELCOME,
            parse_mode = 'HTML',
            reply_markup = agree_button
        )
    else:
        await message.answer(
            text = IF_USER_HAVE_ACCOUNT +'\n'+ UPDATE_MESSAGE
        )
        logging.info(f'User {message.from_user.id} authorization')