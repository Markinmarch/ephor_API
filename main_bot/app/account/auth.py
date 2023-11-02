from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from core.setting import dp
from main_bot.sql_db.users_db import users
from main_bot.utils.commands import set_commands
from main_bot.utils.state import UserForm


@dp.message(CommandStart())
async def start_bot(message: types.Message, state: FSMContext) -> None:
    if users.checking_users(message.from_user.id) == False:
        await set_commands(bot = message.bot)
        await state.set_state(UserForm.name)
        await message.answer(
            text = 'Введите своё <b>действительное</b> имя (имя, отчество)'
        )
    else:
        await message.answer(
            text = 'Вы уже авторизованы.'
        )
