from aiogram import types


from telegram_bot.settings.setting import dp
from telegram_bot.utils.keyboards.reply_keyboard import get_phone_user
from telegram_bot.utils.content.text_content import GIVE_PHONE


@dp.callback_query_handler(text = 'give_phone')
async def add_gender__cmd_phone(callback: types.CallbackQuery) -> None:
    '''
    Данный объект запрашивает разрешение на получение
    контактных данных пользователя (телефон аккаунта)
    -----------------------------------------------
    parametrs:
        :message: тип объкета представления.
    '''
    await callback.message.answer(
        text = GIVE_PHONE,
        reply_markup = get_phone_user
    )
