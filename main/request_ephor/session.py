import time
import requests


from main.core.config import URL, PATH, LOGIN, PASSWORD


class Session:

    def __init__(self):
        self.user_login = LOGIN
        self.user_password = PASSWORD
        self.url = URL
        self.path = PATH['auth']
        self.time_zone = 3
        self.id_request = int(time.time())
        self.json = {
                'login': self.user_login,
                'password': self.user_password,
                'time_zone': self.time_zone
            }
        self.headers = {'Content-Type': 'application/json'}

    def login(self, action):
        respond = requests.api.post(
            url = self.url + self.path,
            json = self.json,
            headers = self.headers,
            params = {
                'action': action,
                '_dc': self.id_request
            },
        )
        return respond.headers.get('Set-Cookie').split('; ')[0]
            
    def logout(self, action):
        respond = requests.api.post(
            url = self.url + self.path,
            json = self.json,
            headers = self.headers,
            params = {
                'action': action,
                '_dc': self.id_request
            }
        )
        return respond.status_code
