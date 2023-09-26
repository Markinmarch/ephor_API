from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from telegram_bot.core.setting import dp
from telegram_bot.utils.state import UsersForm


@dp.message(CommandStart())
async def start_bot(message: types.Message, state: FSMContext) -> None:
    await state.set_state(UsersForm.name)
    await message.answer(
        text = 'Введите своё имя (имя, отчество)'
    )
