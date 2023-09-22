import logging
from main.core.setting import logger, main


if __name__ == '__main__':
    try:
        logging.info('--- App has been started ---')
        main()
    except Exception:
        import traceback
        logger.warning(traceback.format_exc())
