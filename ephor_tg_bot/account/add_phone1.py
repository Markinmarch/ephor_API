from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from ephor_tg_bot.core.setting import dp
from ephor_tg_bot.utils.state import UsersForm
from ephor_tg_bot.sql_db.users_db import users



@dp.message(UsersForm.phone)
async def add_phone_cmd_write_DB(message: types.Message, state: FSMContext) -> None:
    await state.update_data(phone = message.contact.phone_number)
    await message.answer(
        text = 'Авторизация завершина',
        reply_markup = types.ReplyKeyboardRemove()
    )

    user_data = await state.get_data()
    user_name, user_phone = user_data['name'], user_data['phone']
    
    users.insert_users(
        user_id = message.from_user.id,
        user_name = user_name,
        user_phone = user_phone
    )
    