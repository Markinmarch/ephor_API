import requests


from main.request.session import Session
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
    
    def request_error(self, path, action, id):
        respond = requests.api.get(
            url = self.url + path,
            params = {
                'action': action,
                '_dc': self.id_request,
                'filter': ('[{"property": "automat_id", "value": %s}]' % id)
            },
            headers = self.headers_request
        )
        self.disconnect
        return respond.json()

    # def check_params_automat(self, path, id):
    #     respond = requests.api.get(

    #     )