from aiogram import types, F
from aiogram.fsm.context import FSMContext


from ...utils.state import TasksForm
from core.setting import dp 


@dp.message(TasksForm.route)
async def descript_task(message: types.Message, state: FSMContext) -> None:
    '''
    После получения номера маршрута, пользователю предлагается написать
    задание для последующей отправки на адрес канала маршрута
        Параметры:
            message
                тип представления данных
            state
                машина состояний
    '''
    await state.update_data(route = int(message.text))
    await state.set_state(TasksForm.task)
    await message.answer(
        text = 'Опишите задание 🛠',
        reply_markup = types.ReplyKeyboardRemove()
    )