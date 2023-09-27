import logging
import asyncio
from ephor_tg_bot.core.setting import logger, main_bot


if __name__ == '__main__':
    logging.info('--- Telegram BOT has been started ---')
    try:
        asyncio.run(main_bot())
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())