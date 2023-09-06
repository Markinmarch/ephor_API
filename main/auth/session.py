from aiohttp import ClientSession
import asyncio
from datetime import datetime
import requests

from main.settings.config import URL, PATH, LOGIN, PASSWORD


class Session:

    def __init__(
        self,
        login,
        password
    ):
        self.login = login
        self.password = password
        self.url = URL
        self.path = PATH['auth']
        self.time_zone = 3,
        self.action_in = 'Login',
        self.action_out = 'Logout',
        self.id_request = datetime.now().strftime('%M%H%M%S%f')

    @property
    async def connect(self):
        async with ClientSession(base_url = self.url) as session:
            async with session.post(
                url = self.path,
                json = {
                    'login': self.login,
                    'password': self.password,
                    'time_zone': self.time_zone,
                },
                params = {
                    'action': self.action_in,
                    '_dc': self.id_request
                },
                headers = {'Content-Type': 'application/json'}
            ) as respond:
                return await respond.json(content_type = 'text/html')
            
    @property        
    async def disconnect(self):
        async with ClientSession(self.url) as session:
            async with session.post(
                url = self.path,
                headers = {'Content-Type': 'application/json'},
                json = {
                    'login': self.login,
                    'password': self.password,
                    'time_zone': self.time_zone,
                },
                params = {
                    'action': self.action_out,
                    '_dc': self.id_request
                }
            ) as respond:
                return await respond.json(content_type = 'text/html')

session = Session(
    login = LOGIN,
    password = PASSWORD
)
conn = asyncio.run(session.connect)
disconn = asyncio.run(session.disconnect)

print(conn, disconn)