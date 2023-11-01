'''
Настроечный файл для запуска цикла с ключевыми функциями
'''


import logging
import asyncio
import time
from aiogram import Bot, Dispatcher


from main.core.config import BOT_TOKEN


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
    from main.api.request_ephor import basic_request
    from main.api.respond_ephor.respond_error import RespondError
    
    respond = RespondError(basic_request)
    while True:
        await respond.send_errors()
        await asyncio.sleep(30)

async def main() -> None:
    await asyncio.gather(main_bot(), main_api())
