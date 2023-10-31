import logging
import asyncio
from main.core.setting import logger, main_api, main_bot
from multiprocessing import Process



if __name__ == '__main__':
    try:
        from main import tg_bot, api 
        process_api = Process(target = main_api)
        process_api.start()
        logging.info('--- Ephor API has been started ---')
        process_bot = Process(target = main_bot)
        process_bot.start()
        logging.info('--- Telegram BOT has been started ---')
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())