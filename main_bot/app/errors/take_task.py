from aiogram import types, F


from ...utils.keyboards.inline import ready_task
from ....core.setting import dp 


@dp.callback_query(F.data == 'take_task')
async def take_task(query: types.CallbackQuery) -> None:
    await query.message.answer(
        text = 'Пользователь ?? взял в работу' 
    )
    await query.bot.send_message(
        chat_id = query.from_user.id,
        text = 'Когда работа будет выполнена, нажмите кнопку "Готово"',
        reply_markup = ready_task
    )
    await query.message.delete_reply_markup()