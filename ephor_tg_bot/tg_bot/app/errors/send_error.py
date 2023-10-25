from aiogram import types, F
from aiogram.filters import Command


from ephor_tg_bot.core.setting import dp 
from ephor_tg_bot.core.config import TG_ROUTERS
from ephor_tg_bot.utils.keyboards.inline import take_task

@dp.message(Command('test'))
async def error(
    message: types.Message,
    router: int = 2,
    msg: str = 'testtesttesttesttesttesttesttesttest'
    ) -> None:
    await message.bot.send_message(
        chat_id = TG_ROUTERS[router],
        text = msg,
        reply_markup = take_task
    )
    