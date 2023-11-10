import aiohttp
from typing import Coroutine


from .session import Session


class RequestsServer(Session):
    '''
    Объект осуществляет отправку GET-запросов на сервер
    для получения актуальных данных. Наследуется объект
    Session
    '''
    def __init__(
        self,
        connection: Coroutine,
        disconnection: Coroutine
    ):
        '''
        Устанавливает все необходимые атрибуты для объекта RequestsServer
            Параметры:
            *self
                session: object
                    создание объекта сессии
                connect: Callable
                    вход в систему сервера и создание запроса
                disconnect: Callable
                    выход из системы сервера
                headers_request: dict
                    параметры REST-запроса
        '''
        super().__init__()
        self.connect = connection
        self.disconnect = disconnection
        self.headers_request: dict = {
            'Content-Type': 'application/jso',
            'Host': 'erp.ephor.online',
            'Connection': 'keep-alive',
            'Cookie': self.connect #здесь находится параметр PHPSESSIONID
        }

    async def basic_request(
        self,
        path: str,
        action: str
    ) -> list:
        '''
        Метод отправляет GET-запрос для получения
        данных с сервера без фильтрации. Возвраащет
        список необработанных данных.
        Параметры:
            path: str
                путь к обработчику команды
            action: str
                команда обработчика
        '''
        async with aiohttp.ClientSession() as request:
            async with request.get(
            url = self.url + path,
            params = {
                'action': action,
                '_dc': self.id_request
            },
            headers = self.headers_request
            ) as respond:
                self.disconnect
                return await respond.json(content_type = 'text/html')
    
    async def request_params(
        self,
        path: str,
        action: str,
        request_filter: str,
        id: int
    ) -> list:
        '''
        Метод отправляет GET-запрос для получения
        данных с сервера c фильтрацией данных.
        Возвраащет список необработанных данных.
        Параметры:
            path: str
                путь к обработчику команды
            action: str
                команда обработчика
            request_filter: str
                запрос по фильтру
            id: int
                идентификатор запроса по фильтру
        '''
        async with aiohttp.ClientSession() as request:
            async with request.get(
                url = self.url + path,
                params = {
                    'action': action,
                    '_dc': self.id_request,
                    'filter': ('[{"property": "%s", "value": %s}]' %(request_filter, id))
                },
                headers = self.headers_request
            ) as respond:
                self.disconnect
                return await respond.json(content_type = 'text/html')