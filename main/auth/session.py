from aiohttp import ClientSession
import time
import asyncio


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
        self.id_request = time.time()

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
                return respond.headers.get('Set-Cookie').split('; ')[0]
            
    @property        
    async def disconnect(self):
        async with ClientSession(self.url) as session:
            async with session.request(
                method = 'POST',
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
                return respond.status

session = Session(
    login = LOGIN,
    password = PASSWORD
)
connect = asyncio.run(session.connect)
disconnect = asyncio.run(session.disconnect)

print(connect, disconnect)