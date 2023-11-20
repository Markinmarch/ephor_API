from aiogram import types, F
from aiogram.fsm.context import FSMContext


from ...utils.state import TasksForm
from ...sql_db import users
from ...utils.keyboards.inline import take_task
from core.setting import dp 
from core.config import TG_ROUTERS


@dp.message(TasksForm.task)
async def choise_route(message: types.Message, state: FSMContext) -> None:
    '''
    После отправления сообщения с заданием для маршрута, метод публикует в
    зараннее указанном канале маршрута текст задания с данными, кто создал
    задание.
        Параметры:
            message
                тип представления данных
            state:
                машина состояний 
    '''
    await state.update_data(task = message.text)
    user = users.select_name(message.from_user.id)
    task_data = await state.get_data()
    task_route, task_description = task_data['route'], task_data['task']
    await message.bot.send_message(
        chat_id = TG_ROUTERS[task_route],
        text = f'Пользователь {user[0]} создал задание:\n {task_description}',
        reply_markup = take_task
    )
    await message.answer(text = 'Задание отправлено! ✅')