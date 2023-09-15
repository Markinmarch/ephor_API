from aiohttp import ClientSession
import requests
import time


from main.core.config import URL, PATH
from main.request.session import connect, disconnect


class RequestsServer:

    def __init__(self):  
        self.url = URL
        self.time_zone = 3
        self.id_request = int(time.time())

    # @property
    # def request_server(self):
    #     respond = requests.api.get(
    #         url = self.url + PATH['state'],
    #         params = {
    #             'action': 'Read',
    #             '_dc': self.id_request
    #         },
    #         headers = {
    #             'Content-Type': 'application/jso',
    #             'Host': 'erp.ephor.online',
    #             'Connection': 'keep-alive',
    #             'Cookie': connect
    #         }
    #     )
    #     return respond.json()

    @property  
    async def request_server(self):
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
    
    # def check_error(self, id):
    #     respond = requests.api.get(
    #         url = self.url + PATH['state'],
    #         params = {
    #             'action': 'Read',
    #             '_dc': self.id_request,
    #             'filter': ('[{"property": "automat_id", "value": %s}]' % id)
    #         },
    #         headers = {
    #             'Content-Type': 'application/jso',
    #             'Host': 'erp.ephor.online',
    #             'Connection': 'keep-alive',
    #             'Cookie': connect
    #         }
    #     )
    #     return respond.json()

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
