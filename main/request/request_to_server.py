from aiohttp import ClientSession
import asyncio
import time


from main.core.config import URL, PATH
from main.request.session import connect, disconnect


class Requests_automat:

    def __init__(self):  
        self.url = URL
        self.time_zone = 3
        self.id_request = int(time.time())
        
    async def request_automat(self):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url = PATH['state'],
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': 'Read',
                    '_dc': self.id_request
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')
        
    async def check_error(self, id):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url =  PATH['error'],
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': 'Read',
                    '_dc': self.id_request,
                    'filter': ('[{"property": "automat_id", "value": %s}]' % id)
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')
