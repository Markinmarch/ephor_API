'''
Настроечный файл для запуска цикла с ключевыми функциями
'''


import logging
import asyncio
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

async def main_bot() -> None:
    from main.tg_bot import app
    from main.api.request_ephor import basic_request
    from main.api.respond_ephor.respond_error import RespondError
    from main.api.request_ephor.session import Session

    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling(bot))
    loop.create_task(Session().login())
    # respond = RespondError(basic_request)
    # loop.create_task(respond)
    loop.run_forever()
    # await dp.start_polling(bot)




# import logging
# import time
# import asyncio


# logging.basicConfig(
#     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level = logging.INFO
# )
# logger = logging.getLogger(__name__)


# def main():
#     from main.api.request_ephor import basic_request
#     from main.api.respond_ephor.respond_error import RespondError

#     respond = RespondError(basic_request)
#     asyncio.run(respond.send_errors())

    # from main.api import respond_ephor
    # while True:
    #     # try:
    #     asyncio.run(respond_ephor._get_respond_error.send_errors())
    #         # respond_ephor.respond_coins.RespondCoinsCount().send_coins_count
    #         # respond_ephor.signal_appeared.StatusSignalOK().send_signal_appeared
    #         # respond_ephor.respond_no_signal.RespondErrorSignal().send_signal_error
    #     # await asyncio.sleep(60)
    #     # except:
    #         # logging.info('--- Server or web has been breack, please whait to connect ---')
    #         # time.sleep(180)
    #         # continue