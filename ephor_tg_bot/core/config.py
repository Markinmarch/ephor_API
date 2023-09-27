import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'config.env')

CHANNEL_ID = os.getenv('CHANNEL_ID', '')

BOT_URL = 'https://t.me/SevCoffe_bot'

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

TG_ROUTE_1 = None
TG_ROUTE_2 = None
TG_ROUTE_3 = None
TG_ROUTE_4 = None
TG_ROUTE_5 = None
TG_ROUTE_6 = None
TG_ROUTE_7 = None

ADMIN_IDS = [
    805875522
]

DB_PATH = 'ephor_tg_bot/sql_db'

DB_NAME = 'ephor_API'