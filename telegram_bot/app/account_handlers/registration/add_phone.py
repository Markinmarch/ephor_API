import logging
from aiogram import types
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import CHANNEL_ID
from telegram_bot.sql_db.users_db import users
from telegram_bot.utils.state import AddUser
from telegram_bot.utils.commands import set_commands_for_users
from telegram_bot.utils.content.text_content import UPDATE_MESSAGE, OUTSIDER_MESSAGE


@dp.message_handler(state = AddUser.phone, content_types = types.ContentType.CONTACT)
async def add_phone__cmd_finish(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект реализует получение действительного номера телефона.
    Если код страны не российский (не начинается на "+7"), то пользователь
    автоматически блокируется, но всё равно записывается в SQL
    -------------------------------------------------------------------------------------
    parametrs:
        :state: параметр состояния конечного автомата (FSMContext) телефона пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :content_types: параметр формата получаемых данных.
        :message: тип объкета представления.
    '''
    # записываем телефон пользователя
    # при регистрации с компа при вызове телефона пользователя - выдаёт "+7"
    # а при регистрации с телефона, телефон возвращает без "+"
    if message.contact.phone_number[0] == '7' or message.contact.phone_number[0:2] == '+7':
        await state.update_data(phone = int(message.contact.phone_number))
        await set_commands_for_users(bot = message.bot)
        await message.answer(
            text = UPDATE_MESSAGE,
            reply_markup = types.ReplyKeyboardRemove()
        )
        logging.info(f'User {message.from_user.id} authorization')
    #автоматический бан, если код телефона не российский
    else:
        await state.update_data(phone = int(message.contact.phone_number))
        await message.answer(
            text = OUTSIDER_MESSAGE,
            reply_markup = types.ReplyKeyboardRemove()
        )
        await message.bot.ban_chat_member(
            chat_id = CHANNEL_ID,
            user_id = message.from_user.id
        )
        logging.info(f'User {message.from_user.id} blocked')

    #запись данных в SQL
    user_data = await state.get_data()
    user_name, user_age, user_phone = user_data['name'], user_data['age'], user_data['phone']
    if user_data['gender'] == 'Мужской':
        user_gender = 1
    if user_data['gender'] == 'Женский':
        user_gender = 0
    users.insert_users(
        user_id = message.from_user.id,
        user_name = user_name,
        user_age = user_age,
        user_gender = user_gender,
        user_phone = user_phone
    )
    await state.finish()
