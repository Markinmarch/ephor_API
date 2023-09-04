import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'main/settings/config.env')


LOGIN = os.getenv('LOGIN', '')

PASSWORD = os.getenv('PASSWORD', '')

URL = 'https://erp.ephor.online/'

CONNECTION = 'keep-alive'

PATH = {
    'auth': 'api/2.0/Auth.php'
}

