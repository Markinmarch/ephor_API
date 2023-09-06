from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import TIMEOUT_MESSAGES
from telegram_bot.utils.state import AddUser
from telegram_bot.utils.keyboards.reply_keyboard import choose_gender
from telegram_bot.utils.content.text_content import INTERRUPTION_MESSAGE, REGISTRATION_MESSAGE


@dp.message_handler(state = AddUser.age)
async def add_age__cmd_gender(message: types.Message, state: FSMContext) -> None:
    '''
    Данный объект записывает в состояние State()
    возраст нового пользователя и переходит к следующему
    состоянию, запрашивающему пол пользователя
    -----------------------------------------------
    parametrs:
        :state: параметр состояния конечного автомата (FSMContext) возраста пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''    
    await state.update_data(age = int(message.text))
    await AddUser.next()
    await message.answer(
        text = REGISTRATION_MESSAGE['add_gender'],
        reply_markup = choose_gender
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['registration']['gender'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddUser:gender':
            raise KeyError
    except KeyError:
        await message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()