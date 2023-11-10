from aiogram import types, F


from ...sql_db.users_db import users
from ...utils.state import UserForm
from ....core.setting import dp


@dp.message(UserForm.name)
async def add_name(message: types.Message) -> None:
    users.insert_users(
        user_id = message.from_user.id,
        user_name = message.text
    )
    await message.answer(
        text = 'Авторизация успешна.'
    )
    await message.bot.send_animation(
        chat_id = message.from_user.id,
        animation = 'CAACAgIAAxkBAAEKZnRlFDmKVSml19qx0Y1QVn4OxspjNAACTgMAArrAlQUJVun81CkD9jAE',
        caption = 'Авторизация завершена',
    )
