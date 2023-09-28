import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'config.env')

CHANNEL_ID = os.getenv('CHANNEL_ID', '')

BOT_URL = 'https://t.me/SevCoffe_bot'

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

TG_ROUTERS = {
    1: -1001943728686,
    2: -1001887757924,
    3: -1001731361700,
    4: -1001984367295,
    5: -1001897362925,
    6: -1001727560908,
    7: -1001962668626
}

ADMIN_IDS = [
    805875522
]

DB_PATH = 'ephor_tg_bot/sql_db'

DB_NAME = 'ephor_API'