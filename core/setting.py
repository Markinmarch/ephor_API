'''
Настроечный файл для запуска цикла с ключевыми функциями
'''

import time, datetime, logging, asyncio
from aiogram import Bot, Dispatcher


from core.config import BOT_TOKEN


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)

bot = Bot(
    token = BOT_TOKEN,
    parse_mode = 'HTML'
)

dp = Dispatcher()


#main func
async def main_bot() -> None:
    logging.info('--- Telegram BOT has been started ---')
    await dp.start_polling(bot)

async def main_api() -> None:
    from main_api.respond_ephor import (
        appeared_signal,
        responder_error,
        responder_coins,
        responder_error_signal,
        # responder_door_status
    )

    logging.info('--- Ephor API has been started ---')
    while True:
        try:
            now_hour = datetime.datetime.now().hour
            await responder_error.send_errors()
            await responder_coins.send_coins_count()
            await appeared_signal.send_signal_appeared()
            if 8 <= now_hour <= 21:
                await responder_error_signal.send_signal_error()
            # if 8 > now_hour >= 21:
            #     await responder_door_status.send_door_status()
            await asyncio.sleep(60)
        except:
            time.sleep(120)
            continue