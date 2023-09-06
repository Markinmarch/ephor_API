from aiogram import types


from telegram_bot.settings.setting import dp
from telegram_bot.utils.state import AddUser
from telegram_bot.utils.keyboards.reply_keyboard import choose_gender
from telegram_bot.utils.content.text_content import FILTERS_MESSAGE


@dp.message_handler(
    lambda message: message.text.isalpha() is False,
    state = AddUser.name
)
async def check_name(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['registration_user']['name_filter'])

@dp.message_handler(
    lambda message: message.text.isdigit() is False,
    state = AddUser.age
)
async def check_age(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['registration_user']['age_filter'])

@dp.message_handler(
    lambda message: message.text not in [button[0]['text'] for button in choose_gender['keyboard']],
    state = AddUser.gender
)
async def check_gender(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['registration_user']['gender_filter'])
