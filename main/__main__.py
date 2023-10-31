import logging
import asyncio
from main.core.setting import logger, main_api, main_bot
from multiprocessing import Process


# if __name__ == '__main__':
#     logging.info('--- Telegram BOT has been started ---')
#     try:
#         main_bot()
#     except Exception:
#         import traceback
#         logger.warning(traceback.format_exc())


# from main.core.setting import logger, main


if __name__ == '__main__':
    try:
        logging.info('--- App has been started ---')
        process_api = Process(target = main_api)
        process_api.start()
        process_bot = Process(target = main_bot)
        process_bot.start()
        process_api.join()
        process_bot.join()
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())