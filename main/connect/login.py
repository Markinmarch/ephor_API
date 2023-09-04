import aiohttp
import asyncio
from datetime import datetime


from main.settings.config import URL, PATH, LOGIN, PASSWORD


async def connect():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url = URL+PATH['auth'],
            headers = {'Content-Type': 'application/json'},
            json = {
                'login': LOGIN,
                'password': PASSWORD
            },
            params = {
                'action': 'Login',
                'time_zone': 3,
                '_dc': datetime.now().strftime('%Y%M%H%M%S%mS')
            }
        ) as respond:
            return await respond.json(content_type = 'text/html')
asyncio.run(connect())
print(asyncio.run(connect()))
