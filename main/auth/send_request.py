from aiohttp import ClientSession
import asyncio
import time
from datetime import datetime


from main.settings.config import URL, PATH, LOGIN, PASSWORD
from main.auth.session import conn, disconn


class Requests_automat:

    def __init__(self):
        # self.login = login
        # self.password = password
        self.type = 1
        self.url = URL
        self.path = PATH['automat']
        self.time_zone = 3,
        self.action_automat = 'ReadAutomatModel'

    async def request(self):
        async with ClientSession() as session:
            async with session.get(
                url = self.url + self.path,
                headers = {'Content-Type': 'application/json'},
                json = {
                    'type': self.type,
                },
                params = {
                    'action': self.action_automat,
                    'time_zone': self.time_zone,
                    '_dc': datetime.now().strftime('%Y%M%H%M%S%mS'),
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive'
                }
            ) as respond:
                return await respond.json(content_type = 'text/html')
        

request = asyncio.run(Requests_automat().request())

