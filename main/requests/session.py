from aiohttp import ClientSession
import time
import asyncio


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
    async def login(self):
        async with ClientSession(base_url = self.url) as session:
            async with session.post(
                url = self.path,
                json = {
                    'login': self.user_login,
                    'password': self.user_password,
                    'time_zone': self.time_zone,
                },
                params = {
                    'action': self.action_in,
                    '_dc': self.id_request
                },
                headers = {'Content-Type': 'application/json'}
            ) as respond:
                return respond.headers.get('Set-Cookie').split('; ')[0]
            
    @property        
    async def logout(self):
        async with ClientSession(self.url) as session:
            async with session.post(
                url = self.path,
                headers = {'Content-Type': 'application/json'},
                json = {
                    'login': self.user_login,
                    'password': self.user_password,
                    'time_zone': self.time_zone,
                },
                params = {
                    'action': self.action_out,
                    '_dc': self.id_request
                }
            ) as respond:
                return respond.status

session = Session(
    user_login = LOGIN,
    user_password = PASSWORD
)
connect = asyncio.run(session.login)
disconnect = asyncio.run(session.logout)

# print(connect, disconnect)