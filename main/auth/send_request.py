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
                params = {
                    'id': '1',
                    'type': self.type,
                    'action': self.action_automat,
                    '_dc': datetime.now().strftime('%Y%M%H%M%S%mS')
                }
            ) as respond:
                return await respond.json(content_type = 'text/html')
        

request = asyncio.run(Requests_automat().request())
print(request)