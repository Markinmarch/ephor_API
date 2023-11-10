from aiogram import types, F


from ....core.setting import dp 
from ....core.config import TG_ROUTERS


@dp.callback_query(F.data == 'ready_task')
async def task_complete(
    query: types.CallbackQuery,
    router: int = 2,
    msg: str = 'Пользователем ?? задача по автомату ?? выполнена'
) -> None:
    await query.bot.send_message(
        chat_id = TG_ROUTERS[router],
        text = msg
    )
    await query.message.delete_reply_markup()