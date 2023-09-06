from aiogram import types


from telegram_bot.settings.setting import dp
from telegram_bot.utils.keyboards.reply_keyboard import direction_detection_buttons
from telegram_bot.utils.state import AddPost
from telegram_bot.utils.text_content import FILTERS_MESSAGE

    
@dp.message_handler(
    lambda message: len(message.text) > 20,
    state = AddPost.title
)
async def repeat_enter_title(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_title'])

@dp.message_handler(
    lambda message: len(message.text) < 20,
    state = AddPost.text
)
async def repeat_enter_text(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_text'])

@dp.message_handler(
    lambda message: message.text not in [button[0]['text'] for button in direction_detection_buttons['keyboard']],
    state = AddPost.direction
)
async def repeat_enter_direction(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_direction'])