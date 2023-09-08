from aiohttp import ClientSession
import asyncio
import time
from datetime import datetime


from main.settings.config import URL, PATH, LOGIN, PASSWORD
# from main.auth.session import conn, disconn

sec2 = str(time.time())[11:14]
sec1 = str(time.time())[0:10]
_dc = (int(sec1+sec2))

class Requests_automat:

    def __init__(self):
        # self.login = login
        # self.password = password
        self.type = 1
        self.url = URL
        self.path = PATH['read_all']
        self.time_zone = 3,
        self.action_automat = 'Read'

    async def request(self):
        async with ClientSession() as session:
            async with session.get(
                url = self.url + self.path,
                headers = {
                    'Content-Type': 'application/json',
                    'Cookie': 'PHPSESSID=fb81qrh5t37j4necav8l5r5jn5',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive'
                },
                params = {
                    'type': self.type,
                    'action': self.action_automat,
                    '_dc': _dc
                }
            ) as respond:
                return await respond.json(content_type = 'text/html')
        

request = asyncio.run(Requests_automat().request())
for i in request['data']:
    print((i)['company_name'],'--->',(i)['automat_id'])
# print(len(request['data']))