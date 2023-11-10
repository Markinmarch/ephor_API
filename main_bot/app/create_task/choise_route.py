from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from ...utils.keyboards.reply import route_number
from ...utils.state import TasksForm
from ....core.setting import dp 
from ....core.config import TG_ROUTERS


@dp.message(Command('create_task'))
async def choise_route(message: types.Message, state: FSMContext) -> None:
    await state.set_state(TasksForm.route)
    await message.answer(
        text = 'Выберите номер маршрута ⤵',
        reply_markup = route_number
    )
