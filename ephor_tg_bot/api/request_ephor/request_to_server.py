# import requests
import asyncio
import aiohttp
from typing import Callable


from main.request_ephor.session import Session
from main.core.config import ACTION


class RequestsServer(Session):
    '''
    Объект осуществляет отправку GET-запросов на сервер
    для получения актуальных данных. Наследуется объект
    Session
    '''
    def __init__(self):
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
        self.session: object = Session()
        self.connect: Callable = asyncio.run(self.session.login(action = ACTION['login']))
        self.disconnect: Callable = asyncio.run(self.session.logout(action = ACTION['logout']))
        self.headers_request: dict = {
            'Content-Type': 'application/jso',
            'Host': 'erp.ephor.online',
            'Connection': 'keep-alive',
            'Cookie': self.connect #здесь находится параметр PHPSESSIONID
        }

    # def basic_request(
    #         self,
    #         path,
    #         action
    # ) -> list:
    #     '''
    #     Метод отправляет GET-запрос для получения
    #     данных с сервера без фильтрации. Возвраащет
    #     список необработанных данных.
    #     Параметры:
    #         path: str
    #             путь к обработчику команды
    #         action: str
    #             команда обработчика
    #     '''
    #     respond = requests.api.get(
    #         url = self.url + path,
    #         params = {
    #             'action': action,
    #             '_dc': self.id_request
    #         },
    #         headers = self.headers_request
    #     )
    #     self.disconnect
    #     return respond.json()
    
    # def request_params(
    #     self,
    #     path: str,
    #     action: str,
    #     request_filter: str,
    #     id: int
    # ) -> list:
    #     '''
    #     Метод отправляет GET-запрос для получения
    #     данных с сервера c фильтрацией данных.
    #     Возвраащет список необработанных данных.
    #     Параметры:
    #         path: str
    #             путь к обработчику команды
    #         action: str
    #             команда обработчика
    #         request_filter: str
    #             запрос по фильтру
    #         id: int
    #             идентификатор запроса по фильтру
    #     '''
    #     respond = requests.api.get(
    #         url = self.url + path,
    #         params = {
    #             'action': action,
    #             '_dc': self.id_request,
    #             'filter': ('[{"property": "%s", "value": %s}]' %(request_filter, id))
    #         },
    #         headers = self.headers_request
    #     )
    #     self.disconnect
    #     return respond.json()

    async def basic_request(
        self,
        path,
        action
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