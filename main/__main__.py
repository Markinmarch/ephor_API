import logging
import asyncio
from main.core.setting import logger, main


if __name__ == '__main__':

    try:
        from main import tg_bot, api 
        asyncio.run(main())

    except Exception:
        import traceback
        logger.warning(traceback.format_exc())