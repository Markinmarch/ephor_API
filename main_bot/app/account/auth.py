from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from ...sql_db.users_db import users
from ...utils.commands import set_commands
from ...utils.state import UserForm
from ....core.setting import dp


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
