import logging


from aiogram import Bot, Dispatcher


from ephor_tg_bot.core.config import BOT_TOKEN


logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
logger = logging.getLogger(__name__)

bot = Bot(
    token = BOT_TOKEN,
    parse_mode = 'HTML'
)

dp = Dispatcher()

async def main_bot() -> None:
    from ephor_tg_bot import account
    await dp.start_polling(bot)