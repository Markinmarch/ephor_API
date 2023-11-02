'''
Настроечный файл для запуска цикла с ключевыми функциями
'''


import logging
import asyncio
import time
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
    logging.info('--- Ephor API has been started ---')
    from main_api.request_ephor import basic_request
    from main_api.respond_ephor.respond_error import RespondError
    from main_api.respond_ephor.respond_coins import RespondCoinsCount
    
    respond_error = RespondError(basic_request)
    respond_coins = RespondCoinsCount(basic_request)

    while True:
        try:
            await respond_error.send_errors()
            await respond_coins.send_coins_count()
            await asyncio.sleep(60)
        except:
            time.sleep(120)
            continue