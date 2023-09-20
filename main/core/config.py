import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'main/core/config.env')


LOGIN = os.getenv('LOGIN', '')

PASSWORD = os.getenv('PASSWORD', '')

CHANNEL_ID = os.getenv('CHANNEL_ID', '')

BOT_TOKEN = os.getenv('BOT_TOKEN', '')

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
    'error': '/api/2.1/report/automat/Error.php'
}

ACTION = {
    'read': 'Read',
    'login': 'Login',
    'logout': 'Logout'
}

