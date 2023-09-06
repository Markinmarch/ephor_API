from aiogram import types


from telegram_bot.settings.setting import dp
from telegram_bot.utils.keyboards.reply_keyboard import canseled
from telegram_bot.utils.text_content import GIVE_NAME
from telegram_bot.utils.state import AddUser


@dp.message_handler(commands = ['start'])
async def user_verification(message: types.Message) -> None:
    '''
    Данный объект инициализирует состояние State()
    и запрашивает имя нового пользователя
    -----------------------------------------------
    parametrs:
        :text: фильтр обратного вызова обработчика
        :message: тип объекта представления
    '''
    await AddUser.name.set()
    await message.answer(
        text = GIVE_NAME,
        reply_markup = canseled
    )
