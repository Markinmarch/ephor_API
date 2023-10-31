'''
Настроечный файл для запуска цикла с ключевыми функциями
'''


import logging
import asyncio
import time
from aiogram import Bot, Dispatcher


from main.core.config import BOT_TOKEN
from main.api.request_ephor import basic_request
from main.api.respond_ephor.respond_error import RespondError



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




def main_bot() -> None:
    asyncio.run(dp.start_polling(bot))

# def main_api() -> None:

#     respond = RespondError(basic_request)
    
#     while True:
#         asyncio.run(respond.send_errors())
#         time.sleep(30)
