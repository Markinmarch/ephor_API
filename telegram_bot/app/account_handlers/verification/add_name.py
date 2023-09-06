from aiogram import types
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.utils.state import AddUser
from telegram_bot.utils.keyboards.reply_keyboard import get_phone_user
from telegram_bot.utils.text_content import GIVE_PHONE


@dp.message_handler(state = AddUser.name)
async def add_name__cmd_age(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    имя нового пользователя и переходит к следующему
    состоянию, запрашивающему возраст пользователя
    -----------------------------------------------
    parametrs:
        :state: параметр состояния конечного автомата (FSMContext) имени пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    async with state.proxy() as user_data:
        user_data['name'] = message.text
    await AddUser.next()
    await message.answer(
        text = GIVE_PHONE,
        reply_markup = get_phone_user
    )
