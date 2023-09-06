from aiogram import types
from aiogram.dispatcher import FSMContext
import asyncio 


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import TIMEOUT_MESSAGES
from telegram_bot.utils.state import AddUser
from telegram_bot.utils.keyboards.reply_keyboard import canseled
from telegram_bot.utils.content.text_content import REGISTRATION_MESSAGE, INTERRUPTION_MESSAGE


@dp.callback_query_handler(text = 'user_agree')
async def cmd_start_registration(callback: types.CallbackQuery, state: FSMContext) -> None:
    '''
    Данный объект инициализирует состояние State()
    и запрашивает имя нового пользователя
    -----------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :callback: тип объекта представления
    '''
    await AddUser.name.set()
    await callback.message.answer(
        text = REGISTRATION_MESSAGE['add_name'],
        reply_markup = canseled
    )    
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['registration']['name'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddUser:name':
            raise KeyError
    except KeyError:
        await callback.message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()