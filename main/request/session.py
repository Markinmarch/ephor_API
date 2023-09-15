import time
import requests


from main.core.config import URL, PATH, LOGIN, PASSWORD


class Session:

    def __init__(
        self,
        user_login,
        user_password
    ):
        self.user_login = user_login
        self.user_password = user_password
        self.url = URL
        self.path = PATH['auth']
        self.time_zone = 3,
        self.action_in = 'Login',
        self.action_out = 'Logout',
        self.id_request = int(time.time())

    @property
    def login(self):
        respond = requests.api.post(
            url = self.url + self.path,
            json = {
                'login': self.user_login,
                'password': self.user_password,
                'time_zone': self.time_zone
            },
            params = {
                'action': self.action_in,
                '_dc': self.id_request
            },
            headers = {
                'Content-Type': 'application/json'
            }
        )
        return respond.headers.get('Set-Cookie').split('; ')[0]
            
    @property
    def logout(self):
        respond = requests.api.post(
            url = self.url + self.path,
            json = {
                'login': self.user_login,
                'password': self.user_password,
                'time_zone': self.time_zone
            },
            params = {
                'action': self.action_out,
                '_dc': self.id_request
            },
            headers = {
                'Content-Type': 'application/json'
            }
        )
        return respond.status_code

session = Session(
    user_login = LOGIN,
    user_password = PASSWORD
)
connect = session.login
disconnect = session.logout
