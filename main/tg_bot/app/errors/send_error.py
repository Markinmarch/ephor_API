from main.core.setting import bot
from main.core.config import TG_ROUTERS
from main.tg_bot.utils.keyboards.inline import take_task


async def send_msg(
    msg: str,
    router: int = 2
) -> None:
    await bot.send_message(
        chat_id = TG_ROUTERS[router],
        text = msg,
        reply_markup = take_task
    )

