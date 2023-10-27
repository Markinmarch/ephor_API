from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from main.core.setting import dp 
from main.core.config import TG_ROUTERS
from main.tg_bot.utils.keyboards.reply import route_number
from main.tg_bot.utils.state import TasksForm


@dp.message(Command('create_task'))
async def choise_route(message: types.Message, state: FSMContext) -> None:
    await state.set_state(TasksForm.route)
    await message.answer(
        text = 'Выберите номер маршрута ⤵',
        reply_markup = route_number
    )
