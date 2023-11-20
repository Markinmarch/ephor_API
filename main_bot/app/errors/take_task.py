from aiogram import types, F


from ...utils.keyboards.inline import ready_task
from ...sql_db import tasks
from core.setting import dp


@dp.callback_query(F.data == 'take_task')
async def take_task(query: types.CallbackQuery) -> None:
    msg = await query.bot.send_message(
        chat_id = query.from_user.id,
        text = f'<b>Когда работа будет выполнена, нажмите кнопку <i>"Готово"</i>:</b>\n\n{query.message.text}',
        reply_markup = ready_task
    )
    tasks.take_task(
        msg_id = query.message.message_id,
        child_msg_id = msg.message_id,
        chat_id = query.message.chat.id,
        user_id = query.from_user.id
    )
    await query.message.delete_reply_markup()