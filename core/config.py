import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'config.env')

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

LOGIN = os.getenv('LOGIN', '')

PASSWORD = os.getenv('PASSWORD', '')

CHANNEL_ID = -1001897240872

BOT_URL = 'https://t.me/SevCoffe_bot'

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
    805875522,
    445402077,
]

DB_PATH = 'datas'

DB_NAME = 'ephor_API'

URL = 'https://erp.ephor.online'

STATE = {
    'error': 0,
    'warning': 1,
    'no connect': 2,
    'ok': 3,
    'no modem': 4
}

PATH = {
    'auth': '/api/2.0/Auth.php',
    'automat': '/api/2.0/automat/Automat.php',
    'state': '/api/2.1/report/automat/State.php',
    'error': '/api/2.1/report/automat/Error.php',
    'coins': '/api/2.1/automat/Device.php',
    'event': '/api/2.1/report/automat/Event.php'
}

FILTER = {
    'automat': 'automat_id',
    'device': 'device_id'
}

ACTION = {
    'read': 'Read',
    'read_all': 'ReadAll',
    'login': 'Login',
    'logout': 'Logout',
    'automat_device': 'ReadAutomatDevice'
}

ERRORS = [
    'Автомат долго не переходит в режим продаж',
    'Автомат долго не выходил в режим продаж',
    'Автомат не принимал карты более 2 часов',
    'Автомат не принимал карты более 5 часов'
]

SPEC_ERROR = 'Безналичная оплата продукта'

SIGNAL_ERROR = 'Нет связи с автоматом!'

DESCRIPTION = {
    'open_door': 'Дверь открыта',
    'close_door': 'Дверь закрыта'
}