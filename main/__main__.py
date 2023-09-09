import asyncio


from main.core.setting import logger, main


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())