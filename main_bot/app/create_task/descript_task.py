from aiogram import types, F
from aiogram.fsm.context import FSMContext


from core.setting import dp 
from main_bot.utils.state import TasksForm


@dp.message(TasksForm.route)
async def descript_task(message: types.Message, state: FSMContext) -> None:
    await state.update_data(route = int(message.text))
    await state.set_state(TasksForm.task)
    await message.answer(
        text = 'Опишите задание 🛠',
        reply_markup = types.ReplyKeyboardRemove()
    )