from aiogram import types, F
from aiogram.fsm.context import FSMContext


from ephor_tg_bot.core.setting import dp 
from ephor_tg_bot.core.config import TG_ROUTERS
from ephor_tg_bot.utils.state import TasksForm
from ephor_tg_bot.sql_db.users_db import users
from ephor_tg_bot.utils.keyboards.inline import take_task


@dp.message(TasksForm.task)
async def choise_route(message: types.Message, state: FSMContext) -> None:
    await state.update_data(task = message.text)
    user = users.select_name(user_id = message.from_user.id)
    task_data = await state.get_data()
    task_route, task_description = task_data['route'], task_data['task']
    await message.bot.send_message(
        chat_id = TG_ROUTERS[task_route],
        text = f'Пользователь {user[0]} создал задание:\n {task_description}',
        reply_markup = take_task
    )
    await message.answer(text = 'Задание отправлено! ✅')