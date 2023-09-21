import logging
import time


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    
    from main import request_ephor
    while True:
        request_ephor.respond_error.Responders().listen_errors
        time.sleep(40)
