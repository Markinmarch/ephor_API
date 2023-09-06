import logging
from aiogram import types
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.sql_db.users_db import users
from telegram_bot.utils.state import AddUser
from telegram_bot.utils.commands import set_commands_for_users
from telegram_bot.utils.content.text_content import VERIFICATION


@dp.message_handler(state = AddUser.phone, content_types = types.ContentType.CONTACT)
async def add_phone__cmd_finish(message: types.Message, state = FSMContext) -> None:
    '''
    Данный объект реализует получение действительного номера телефона.
    -------------------------------------------------------------------------------------
    parametrs:
        :state: параметр состояния конечного автомата (FSMContext) телефона пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :content_types: параметр формата получаемых данных.
        :message: тип объкета представления.
    '''
    # записываем телефон пользователя
    await state.update_data(phone = int(message.contact.phone_number))
    await set_commands_for_users(bot = message.bot)
    await message.answer(
        text = VERIFICATION,
        reply_markup = types.ReplyKeyboardRemove()
    )
    logging.info(f'User {message.from_user.id} authorization')

    #запись данных в SQL
    user_data = await state.get_data()
    user_name, user_phone = user_data['name'], user_data['phone']
    users.insert_users(
        user_id = message.from_user.id,
        user_name = user_name,
        user_phone = user_phone
    )
    await state.finish()
