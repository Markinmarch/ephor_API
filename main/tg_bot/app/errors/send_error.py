# from aiogram import types, F
from aiogram.filters import Command
import asyncio


from main.core.setting import bot, dp
from main.core.config import TG_ROUTERS
from main.tg_bot.utils.keyboards.inline import take_task
from main.api.respond_ephor import stts


# async def send_msg(
#     msg: str,
#     router: int = 2    
# ) -> None:
#     await bot.send_message(
#         chat_id = TG_ROUTERS[router],
#         text = msg,
#         reply_markup = take_task
#     )

@dp.message(Command('test'))
async def send_msg(
        msg: str = stts,
        router: int = 2
) -> None:
    await bot.send_message(
        chat_id = TG_ROUTERS[router],
        text = msg,
        reply_markup = take_task
    )

