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
def main_bot() -> None:
    asyncio.run(dp.start_polling(bot))

def main_api():
    from main.api.request_ephor import basic_request
    from main.api.respond_ephor.respond_error import RespondError

    respond = RespondError(basic_request)
    asyncio.run(respond.send_errors())
    logging.info('123')

    while True:
        try:
            asyncio.run(respond.send_errors())
            time.sleep(40)
        except:
            time.sleep(60)
            continue
