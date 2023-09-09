from aiohttp import ClientSession
import asyncio
import time


from main.core.config import URL, PATH
from main.requests.session import connect, disconnect


class Requests_automat:

    def __init__(self):
        self.url = URL
        self.path = PATH['read_all']
        self.time_zone = 3,
        self.id_request = int(time.time())
        self.action_automat = 'Read'

    @property
    async def request(self):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url = self.path,
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': self.action_automat,
                    '_dc': self.id_request
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')
        

request = asyncio.run(Requests_automat().request)


# print(request['data'])
lst = [i['automat_state'] for i in request['data']]
print(lst.count(1))