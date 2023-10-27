import logging
import asyncio
from main.core.setting import logger, main_bot


if __name__ == '__main__':
    logging.info('--- Telegram BOT has been started ---')
    try:
        asyncio.run(main_bot())
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())


# import logging
# from main.core.setting import logger, main


# if __name__ == '__main__':
#     try:
#         logging.info('--- App has been started ---')
#         main()
#     except Exception:
#         import traceback
#         logger.warning(traceback.format_exc())