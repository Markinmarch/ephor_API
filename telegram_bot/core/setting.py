import logging


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from telegram_bot.core.config import BOT_TOKEN


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

bot = Bot(
    token = BOT_TOKEN,
    parse_mode = 'HTML'
)

dp = Dispatcher()

async def main_bot() -> None:
    from telegram_bot import account
    await dp.start_polling(bot)