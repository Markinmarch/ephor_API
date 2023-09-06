from aiogram import types
import logging


from telegram_bot.settings.setting import dp
from telegram_bot.utils.keyboards.inline_keyboard import start_registration_button
from telegram_bot.utils.content.text_content import UNREGISTRED_USER, IF_USER_HAVE_ACCOUNT, UPDATE_MESSAGE
from telegram_bot.sql_db.users_db import users
from telegram_bot.utils.commands import set_commands_for_new_user, set_commands_for_users


@dp.message_handler(commands = ['start'])
async def user_verification(message: types.Message) -> None:
    '''
    Данный объект проверяет пользователя на наличие
    его учётной запси по его id при первичном запросе
    к телеграм-боту
    -----------------------------------------------
    parametrs:
        :commands: команда вызова обработчика
        :message: тип объкета представления.
    '''
    if users.checking_users(message.from_user.id) == False:
        await set_commands_for_users(bot = message.bot)
        await message.answer(
            text = 'Пройдите верификацию для дальнейшего взаимодействия с ботом',
            reply_markup = start_registration_button
        )
    else:
        await set_commands_for_users(bot = message.bot)
        await message.answer(
            text = UPDATE_MESSAGE,
        )
        logging.info(f'User {message.from_user.id} authorization')
