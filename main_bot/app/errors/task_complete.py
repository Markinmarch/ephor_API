from aiogram import types, F


from ...sql_db.users_db import users
from core.setting import dp 
from core.config import TG_ROUTERS


@dp.callback_query(F.data == 'ready_task')
async def task_complete(
    query: types.CallbackQuery,
    router: int,
    msg: str
) -> None:
    user_name = users.select_name(query.from_user.id)
    automat_id = 'None'
    router = 1
    msg = f'Пользователем {user_name} задача по автомату {automat_id} выполнена'
    await query.bot.send_message(
        chat_id = TG_ROUTERS[router],
        text = msg
    )
    await query.message.delete_reply_markup()

