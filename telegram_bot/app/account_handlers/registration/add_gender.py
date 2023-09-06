from aiogram import types
import asyncio


from telegram_bot.settings.setting import dp
from telegram_bot.settings.config import TIMEOUT_MESSAGES
from telegram_bot.utils.keyboards.reply_keyboard import get_phone_user
from telegram_bot.utils.content.text_content import INTERRUPTION_MESSAGE, REGISTRATION_MESSAGE


@dp.m
async def add_gender__cmd_phone(message: types.Message) -> None:
    '''
    Данный объект записывает в состояние State()
    пол нового пользователя и переходит к следующему
    состоянию, запрашивающему разрешение на получение
    контактных данных пользователя (телефон аккаунта)
    -----------------------------------------------
    parametrs:
        :state: параметр состояния конечного автомата (FSMContext) пола пользователя
        url https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/index.html
        :message: тип объкета представления.
    '''
    await message.answer(
        text = REGISTRATION_MESSAGE['add_phone'],
        reply_markup = get_phone_user
    )
