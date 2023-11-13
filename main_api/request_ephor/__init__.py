'''
Модуль создания сессии для зарегестрированных пользователей
и запроса данных с сервера по указанным параметрам
    Параметры:
        connection: Courutine
            открытие сесси, возвращает PHPSESSIONID от сервера для работы с ресурсом
        disconndection: Courutine
            закрытие сессии, возвращает status id = 200 ("OK")
        ephor_request: Object
            устанавливает связь с сервером, принимает параметры connection, disconnection
        states_request: Courutine
            запрашивает состояние автоматов для контроля на них ошибок,
            принимает параметры path и action
'''


import asyncio


from . import session
from . import request_to_server


from .session import Session
from .request_to_server import RequestsServer
from core.config import PATH, ACTION


connection = asyncio.run(Session().login())
disconnection = asyncio.run(Session().logout())

ephor_requset = RequestsServer(connection=connection, disconnection=disconnection)

states_request = asyncio.run(
    ephor_requset.basic_request(
        path = PATH['state'],
        action = ACTION['read']
    )
)

event_request = asyncio.run(
    ephor_requset.basic_request(
        path = PATH['event'],
        action = ACTION['read_all']
    )
)