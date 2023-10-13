'''
Конфигурационный файл для хранения данных
'''


import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'config.env')


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
    'error': '/api/2.1/report/automat/Error.php',
    'coins': '/api/2.1/automat/Device.php'
}

FILTER = {
    'automat': 'automat_id',
    'device': 'device_id'
}

ACTION = {
    'read': 'Read',
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