import requests


from main.request_ephor.session import Session
from main.core.config import ACTION


class RequestsServer(Session):

    def __init__(self):
        super().__init__()
        self.session = Session()
        self.connect = self.session.login(action = ACTION['login'])
        self.disconnect = self.session.logout(action = ACTION['logout'])
        self.headers_request = {
            'Content-Type': 'application/jso',
            'Host': 'erp.ephor.online',
            'Connection': 'keep-alive',
            'Cookie': self.connect
        }

    def request_state(self, path, action):
        respond = requests.api.get(
            url = self.url + path,
            params = {
                'action': action,
                '_dc': self.id_request
            },
            headers = self.headers_request
        )
        self.disconnect
        return respond.json()
    
    def request_params(
        self,
        path: str,
        action: str,
        request_filter: str,
        id: int
    ) -> list:
        respond = requests.api.get(
            url = self.url + path,
            params = {
                'action': action,
                '_dc': self.id_request,
                'filter': ('[{"property": "%s", "value": %s}]' %(request_filter, id))
            },
            headers = self.headers_request
        )
        self.disconnect
        return respond.json()
