import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = 'main/settings/config.env')


LOGIN = os.getenv('LOGIN', '')

PASSWORD = os.getenv('PASSWORD', '')

URL = 'https://erp.ephor.online'

CONNECTION = 'keep-alive'

PATH = {
    'auth': '/api/2.0/Auth.php',
    'automat': '/api/2.0/automat/Automat.php',
    'read_all': '/api/2.1/report/automat/State.php'
}
