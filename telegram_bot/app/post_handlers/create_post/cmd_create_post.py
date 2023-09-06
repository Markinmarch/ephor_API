from aiogram import types
import asyncio
from aiogram.dispatcher import FSMContext


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import TIMEOUT_MESSAGES
from telegram_bot.utils.state import AddPost
from telegram_bot.utils.keyboards.reply_keyboard import direction_detection_buttons
from telegram_bot.utils.content.text_content import INTERRUPTION_MESSAGE, CREATE_POST_MESSAGE


@dp.callback_query_handler(text = 'user_informed')
async def cmd_start_create_post(callback: types.CallbackQuery, state = FSMContext) -> None:
    '''
    Данный объект инициализирует состояние State()
    и предлагает выбрать тему объявления
    -----------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :state: (str) параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await AddPost.direction.set()
    await callback.message.answer(
        text = CREATE_POST_MESSAGE['direction'],
        reply_markup = direction_detection_buttons
    )
    # конструкция для определения времени ожидания ответа от пользователя
    # благодаря осуществляемому способу защищаем сервер от перегрузок
    await asyncio.sleep(TIMEOUT_MESSAGES['create_post']['direction'])
    try:
        current_state = await state.get_state()
        if current_state == 'AddPost:direction':
            raise KeyError
    except KeyError:
        await callback.message.answer(text = INTERRUPTION_MESSAGE)
        await state.finish()