from aiogram import types, F


from ...sql_db import users, tasks
from core.setting import dp
from core.config import TG_ROUTERS


@dp.callback_query(F.data == 'ready_task')
async def task_complete(query: types.CallbackQuery) -> None:
    user_name = users.select_name(query.from_user.id)
    msg_and_chat_ids = tasks.select_task(child_msg_id = query.message.message_id)
    chat_id = msg_and_chat_ids[1]
    msg_id = msg_and_chat_ids[0]
    msg = f'Пользователем {user_name[0]} задача выполнена.'
    await query.bot.send_message(
        chat_id = chat_id,
        text = msg,
        reply_to_message_id = msg_id
    )
    await query.message.delete_reply_markup()
