from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext


from ephor_tg_bot.core.setting import dp
from ephor_tg_bot.utils.state import UsersForm
from ephor_tg_bot.utils.keyboards.reply import get_phone_user


@dp.message(UsersForm.name)
async def add_name_cmd_phone(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name = message.text)
    await state.set_state(UsersForm.phone)
    await message.answer(
        text = 'Подтвердите отправку своего номера телефона',
        reply_markup = get_phone_user
    )