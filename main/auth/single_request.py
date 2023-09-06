import requests
from datetime import datetime


from main.settings.config import *

nt = datetime.now().strftime("%M%H%M%S%f")
def request_auth():
    session = requests.Session()
    conn = session.post(
        url = f"{URL + PATH['auth']}",
        headers = {
            "Content-Type": "application/text"
        },
        auth = {
            "login": LOGIN,
            "password": PASSWORD,
            "time_zone": 3,
        },
        params = {
            "action": "Login",
            "_dc": nt,
        }
    )
    return conn.json()

print(request_auth())

