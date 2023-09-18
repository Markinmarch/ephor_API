import logging


from aiogram import Bot, Dispatcher, executor
# from aiogram. contrib.fsm_storage.redis import RedisStorage2
from aiogram.fsm.storage.redis import RedisStorage

from telegram_bot.settings import config


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)

bot = Bot(
    token = config.BOT_TOKEN,
    parse_mode = 'HTML'
)

storage = RedisStorage()

dp = Dispatcher(
    bot,
    storage = storage
)

def main():
    from telegram_bot import app

    executor.start_polling(
        dp,
        skip_updates = True
    )
