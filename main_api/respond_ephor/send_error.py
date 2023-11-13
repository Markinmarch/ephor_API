from core.setting import bot
from core.config import TG_ROUTERS
from main_bot.utils.keyboards.inline import take_task


async def send_msg(
    msg: str,
    router: int = 2
) -> None:
    '''
    Метод отправляет сообщения об ошибках автоматов в канал маршрута
        Параметры:
            msg: str
                текст сообщения ошибки с данными об автомате
            router: int
                номер маршрута
    '''
    await bot.send_message(
        chat_id = TG_ROUTERS[router],
        text = msg,
        reply_markup = take_task
    )