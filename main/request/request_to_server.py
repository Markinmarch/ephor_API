import requests
import time


from main.core.config import URL, PATH
from main.request.session import connect, disconnect


class RequestsServer:

    def __init__(self):  
        self.url = URL
        self.time_zone = 3
        self.id_request = int(time.time())

    @property
    def request_server(self):
        respond = requests.api.get(
            url = self.url + PATH['state'],
            params = {
                'action': 'Read',
                '_dc': self.id_request
            },
            headers = {
                'Content-Type': 'application/jso',
                'Host': 'erp.ephor.online',
                'Connection': 'keep-alive',
                'Cookie': connect
            }
        )
        disconnect
        return respond.json()
    
    def check_error(self, id):
        respond = requests.api.get(
            url = self.url + PATH['error'],
            params = {
                'action': 'Read',
                '_dc': self.id_request,
                'filter': ('[{"property": "automat_id", "value": %s}]' % id)
            },
            headers = {
                'Content-Type': 'application/jso',
                'Host': 'erp.ephor.online',
                'Connection': 'keep-alive',
                'Cookie': connect
            }
        )
        disconnect
        return respond.json()
