from aiogram import types


from telegram_bot.settings.setting import dp
from telegram_bot.utils.content.text_content import BAD_WORDS, FILTERS_MESSAGE
from telegram_bot.utils.state import AddPost, AddUser

@dp.message_handler(
    lambda message: message.text in BAD_WORDS,
    state = AddUser.all_states
)
async def block_bad_words_in_registration(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['bad_words'])

@dp.message_handler(
    lambda message: message.text in BAD_WORDS,
    state = AddPost.all_states
)
async def block_bad_words_in_posts(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['bad_words'])
