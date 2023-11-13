from aiogram import types, F


from ...utils.keyboards.inline import ready_task
from ...sql_db.users_db import users
from core.setting import dp 


@dp.callback_query(F.data == 'take_task')
async def take_task(query: types.CallbackQuery) -> None:
    user_name = users.select_name(query.from_user.id)
    text = query.message.text
    id = text.split('\n')
    print(id)
    await query.message.answer(
        text = f'Пользователь {user_name[0]} взял в работу:\n{text}' 
    )
    await query.bot.send_message(
        chat_id = query.from_user.id,
        text = 'Когда работа будет выполнена, нажмите кнопку "Готово"',
        reply_markup = ready_task
    )
    await query.message.delete_reply_markup()