import aiohttp
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
        self.action_out = 'Logout'

    async def connect(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = self.url + self.path,
                headers = {'Content-Type': 'application/json', 'Host': 'erp.ephor.online', 'Connection': 'keep-alive'},
                json = {
                    'login': self.login,
                    'password': self.password,
                    'time_zone': self.time_zone,
                },
                params = {
                    'action': self.action_in,
                    '_dc': datetime.now().strftime('%Y%M%H%M%S%f')
                }
            ) as respond:
                return await respond.json(content_type = 'text/html')
            
    async def disconnect(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = URL+PATH['auth'],
                headers = {'Content-Type': 'application/json'},
                json = {
                    'login': self.login,
                    'password': self.password
                },
                params = {
                    'action': self.action_out,
                    'time_zone': self.time_zone,
                    '_dc': datetime.now().strftime('%Y%M%H%M%S%mS')
                }
            ) as respond:
                return await respond.json(content_type = 'text/html')

session = Session(
    login = LOGIN,
    password = PASSWORD
)
conn = asyncio.run(session.connect())
disconn = asyncio.run(session.disconnect())
