import logging
import asyncio
from core.setting import logger, main_api


if __name__ == '__main__':

    try:
        from main_api import request_ephor, respond_ephor
        import core
        asyncio.run(main_api())

    except Exception:
        import traceback
        logger.warning(traceback.format_exc())