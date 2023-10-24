'''
Настроечный файл для запуска цикла с ключевыми функциями
'''


import logging
import time
import asyncio


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    
    from main import respond_ephor
    while True:
        # try:
        asyncio.run(respond_ephor.respond_error.RespondError().send_errors())
            # respond_ephor.respond_coins.RespondCoinsCount().send_coins_count
            # respond_ephor.signal_appeared.StatusSignalOK().send_signal_appeared
            # respond_ephor.respond_no_signal.RespondErrorSignal().send_signal_error
        time.sleep(60)
        # except:
            # logging.info('--- Server or web has been breack, please whait to connect ---')
            # time.sleep(180)
            # continue