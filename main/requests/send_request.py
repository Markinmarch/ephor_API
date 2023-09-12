from aiohttp import ClientSession
import asyncio
import time


from main.core.config import URL, PATH, STATUS, ACTION
from main.requests.session import connect, disconnect


class Requests_automat:

    def __init__(self):  
        self.url = URL
        self.time_zone = 3,
        self.id_request = int(time.time())
        
    async def request_automat(self, path, action):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url = path,
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': action,
                    '_dc': self.id_request
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')
        
    async def check_error(self, path, action, id):
        async with ClientSession(base_url = self.url) as session:
            async with session.get(
                url =  path,#PATH['check_errors'],
                headers = {
                    'Content-Type': 'application/json',
                    'Host': 'erp.ephor.online',
                    'Connection': 'keep-alive',
                    'Cookie': connect,
                },
                params = {
                    'action': action,
                    '_dc': self.id_request,
                    'filter': ('[{"property": "automat_id", "value": %s}]' % id)
                }
            ) as respond:
                disconnect
                return await respond.json(content_type = 'text/html')

request_all = asyncio.run(
    Requests_automat().request_automat(
        path = PATH['state'],
        action = ACTION['read']
    )
)
check_status = [i['automat_state'] for i in request_all['data']]
status_error_count = check_status.count(STATUS['error'])



# check_errors = asyncio.run(Requests_automat().check_error(i['automat_id']))
# print(request_all)

# print(request_all['data'])

errors = [i for i in request_all['data'] if i['automat_state'] == STATUS['no connect']]
for i in errors:
    error = i['automat_id'], i['model_name'], i['point_adress'], i['point_comment'], i['point_name']

    # check_errors = asyncio.run(Requests_automat().check_error(i['automat_id']))
    # for x in check_errors['data']:
    #     print(x['description'])

#0 -> ERROR
#1 -> WARNING
#2 -> NO CONNECTION
#3 -> OK
#4 -> NO MODEM

