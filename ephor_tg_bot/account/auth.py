from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from ephor_tg_bot.core.setting import dp
from ephor_tg_bot.sql_db.users_db import users
from ephor_tg_bot.utils.commands import set_commands
from ephor_tg_bot.utils.state import UserForm


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
