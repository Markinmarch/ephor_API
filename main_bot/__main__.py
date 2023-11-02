import logging
import asyncio
from core.setting import logger, main_bot


if __name__ == '__main__':

    try:
        from main_bot import app, sql_db, utils
        asyncio.run(main_bot())

    except Exception:
        import traceback
        logger.warning(traceback.format_exc())