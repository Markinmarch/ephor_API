from aiogram import types, F


from core.setting import dp 
from main_bot.utils.keyboards.inline import ready_task


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