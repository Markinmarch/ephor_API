import logging
import time


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    
    from main import respond_ephor
    while True:
        try:
            respond_ephor.respond_error.RespondError().listen_errors
            respond_ephor.respond_coins.RespondCoinsCount().listen_coins_count
            respond_ephor.signal_appeared.StatusSignalOK().listen_signal_appeared
            respond_ephor.respond_no_signal.RespondErrorSIGNAL().listen_signal_error
            time.sleep(60)
        except:
            logging.info('--- Server or web has been breack, please whait to connect ---')
            time.sleep(600)
            continue